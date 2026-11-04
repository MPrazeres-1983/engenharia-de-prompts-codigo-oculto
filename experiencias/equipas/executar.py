"""Piloto opt-in de arquiteturas. Apenas servidor local, dados sintéticos, sem ações."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from exemplos.laboratorio.equipas import ClienteLocal, executar, stub  # noqa: E402

# Fixados antes da primeira chamada; não alterados para melhorar resultados.
CASOS = [
    ('E1', 'Recebi os sacos, mas uma camisola ficou pelo caminho.', 'pecas_em_falta', 'POL-01'),
    ('E2', 'Em que dia recebo o dinheiro que pedi de volta?', 'prazo', 'POL-02'),
    ('E3', 'Qual o estado de LAV-001?', 'estado_reclamacao', None),
    ('E4', 'Qual o horário de abertura aos domingos?', 'outro', None),
]
SEEDS = (42, 1337)


def avaliar(registos):
    grupos = defaultdict(list)
    for r in registos:
        grupos[r['modo']].append(r)
    resumo = {}
    for modo, linhas in sorted(grupos.items()):
        corretos = sum(r['resultado']['estado'] == 'concluido'
                       and r['resultado']['saida'] == r['esperado'] for r in linhas)
        resumo[modo] = {'execucoes': len(linhas), 'casos_unicos': len({r['caso'] for r in linhas}),
                        'corretos_categoria_e_fonte': corretos,
                        'encaminhados': sum(r['resultado']['estado'] != 'concluido' for r in linhas),
                        'chamadas_llm': sum(len(r['chamadas']) for r in linhas),
                        'segundos_observados': sum(r['resultado']['segundos'] for r in linhas)}
    return resumo


def main():
    p = argparse.ArgumentParser(__doc__)
    p.add_argument('--base-url', default='http://127.0.0.1:8766')
    p.add_argument('--modelo', default='Qwen2.5-0.5B-Instruct-Q4_K_M')
    p.add_argument('--modelo-ficheiro', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    saidas = args.output/'saidas.jsonl'
    if any(args.output.iterdir()):
        p.error('Pasta não vazia; preservar ensaios anteriores')
    modelo_hash = hashlib.sha256(args.modelo_ficheiro.read_bytes()).hexdigest()
    manifesto = {'data_utc': datetime.now(timezone.utc).isoformat(),
                 'modelo': args.modelo, 'sha256_modelo': modelo_hash,
                 'plataforma': platform.platform(), 'seeds': list(SEEDS),
                 'casos': CASOS, 'inferencias_planeadas': 32,
                 'temperatura': 0.2, 'max_tokens': 96,
                 'runtime': 'llama.cpp b11960', 'threads': 4, 'parallel': 2,
                 'ctx_size_servidor': 8192, 'gpu_layers': 0,
                 'sha256_fonte': {f: hashlib.sha256((RAIZ/f).read_bytes()).hexdigest()
                     for f in ['experiencias/equipas/executar.py', 'exemplos/laboratorio/equipas.py']},
                 'limites': 'Piloto sintético com quatro casos, duas seeds e o mesmo modelo pequeno. '
                 'Sem humanos, teste reservado, efeitos externos ou equivalência de custo entre arquiteturas. '
                 'Segundos incluem fila e execução; não são benchmark isolado de paralelismo.'}
    (args.output/'manifesto.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=2)+'\n')
    registos = []
    for id_, pedido, categoria, fonte in CASOS:
        for i, seed in enumerate(SEEDS):
            modos = ('fluxo', 'unico', 'equipa') if i == 0 else ('fluxo', 'equipa', 'unico')
            for modo in modos:
                cliente = ClienteLocal(args.base_url, args.modelo)
                adaptador = stub if modo == 'fluxo' else cliente
                resultado = executar(pedido, adaptador, modo='unico' if modo == 'fluxo' else modo, seed=seed)
                r = {'caso': id_, 'seed': seed, 'modo': modo, 'pedido': pedido,
                     'utc': datetime.now(timezone.utc).isoformat(),
                     'esperado': {'categoria': categoria, 'fonte': fonte},
                     'resultado': resultado, 'chamadas': cliente.registos}
                registos.append(r)
                with saidas.open('a', encoding='utf-8') as f:
                    f.write(json.dumps(r, ensure_ascii=False)+'\n')
                print(id_, seed, modo, resultado['estado'], flush=True)
    resumo = avaliar(registos)
    (args.output/'resumo.json').write_text(json.dumps(resumo, ensure_ascii=False, indent=2)+'\n')
    manifesto['sha256_saidas'] = hashlib.sha256(saidas.read_bytes()).hexdigest()
    manifesto['inferencias_registadas'] = sum(len(r['chamadas']) for r in registos)
    (args.output/'manifesto.json').write_text(json.dumps(manifesto, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(resumo, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
