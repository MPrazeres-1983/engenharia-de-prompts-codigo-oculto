"""Registo determinístico de software. Zero chamadas a LLM; sem medir tempo."""
import argparse
import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from experiencias.equipas.executar import CASOS  # noqa: E402
from exemplos.laboratorio.equipas import executar, stub  # noqa: E402

REGISTO = Path(__file__).parent/'resultados/offline-2026-11-04.json'


def gerar():
    linhas = []
    for modo in ('fluxo', 'unico', 'equipa'):
        for id_, pedido, categoria, fonte in CASOS:
            r = executar(pedido, stub, modo='unico' if modo == 'fluxo' else modo)
            r.pop('segundos')
            esperado = {'categoria': categoria, 'fonte': fonte}
            linhas.append({'modo': modo, 'caso': id_, 'pedido': pedido,
                           'esperado': esperado, 'resultado': r,
                           'correto': r['estado'] == 'concluido' and r['saida'] == esperado})
    resumo = {modo: {'casos': 4, 'corretos': sum(x['correto'] for x in linhas if x['modo'] == modo),
                     'chamadas_componentes': sum(x['resultado']['chamadas'] for x in linhas if x['modo'] == modo),
                     'chamadas_llm': 0} for modo in ('fluxo', 'unico', 'equipa')}
    return {'tipo': 'ensaio determinístico de software, dados sintéticos, sem LLM ou humanos',
            'data': '2026-11-04', 'linhas': linhas, 'resumo': resumo,
            'limite': 'O mesmo stub em todos os papéis não acrescenta capacidade; não mede qualidade de modelos.'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(__doc__)
    p.add_argument('--verificar', action='store_true')
    args = p.parse_args()
    resultado = gerar()
    if args.verificar:
        if json.loads(REGISTO.read_text()) != resultado:
            raise SystemExit('Registo offline difere da execução')
    else:
        if REGISTO.exists():
            raise SystemExit('Registo existente; não substituir')
        REGISTO.parent.mkdir(parents=True, exist_ok=True)
        REGISTO.write_text(json.dumps(resultado, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(resultado['resumo'], ensure_ascii=False, indent=2))
