"""Valida o pacote demonstrativo: subconjunto simples de frontmatter, não todo YAML."""
import hashlib
import json
from pathlib import Path
import re

PACOTE = Path(__file__).resolve().parents[1] / 'skills/rever-evidencias'


def validar_pacote(pasta=PACOTE):
    pasta = Path(pasta).resolve()
    texto = (pasta / 'SKILL.md').read_text(encoding='utf-8')
    partes = texto.split('---', 2)
    if len(partes) != 3 or partes[0] or not partes[2].strip():
        raise ValueError('Frontmatter ou corpo ausente')
    campos = {}
    for linha in partes[1].strip().splitlines():
        chave, sep, valor = linha.partition(':')
        if not sep or chave in campos:
            raise ValueError('Subconjunto local exige campos escalares únicos')
        campos[chave] = valor.strip()
    nome = campos.get('name', '')
    if (not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', nome) or len(nome) > 64
            or nome != pasta.name):
        raise ValueError('Nome inválido ou diferente da pasta')
    if not 1 <= len(campos.get('description', '')) <= 1024:
        raise ValueError('Descrição ausente ou demasiado longa')
    if 'compatibility' in campos and not 1 <= len(campos['compatibility']) <= 500:
        raise ValueError('Compatibility fora do limite')
    manifesto = json.loads((pasta / 'manifesto.json').read_text(encoding='utf-8'))
    if manifesto.get('versao') != '1.0.0' or not manifesto.get('ficheiros'):
        raise ValueError('Manifesto inválido')
    for relativo, esperado in manifesto['ficheiros'].items():
        ficheiro = (pasta / relativo).resolve()
        if not ficheiro.is_relative_to(pasta) or not ficheiro.is_file():
            raise ValueError('Caminho fora do pacote ou inexistente')
        if hashlib.sha256(ficheiro.read_bytes()).hexdigest() != esperado:
            raise ValueError('Hash diferente: ' + relativo)
    for relativo in ('SKILL.md', 'scripts/validar_fichas.py', 'assets/fichas.json'):
        if relativo not in manifesto['ficheiros']:
            raise ValueError('Recurso não incluído no manifesto')
    return {'nome': nome, 'versao': manifesto['versao'], 'hashes': 'ok',
            'nota': 'Estrutura e integridade; não testa ativação por um agente nem verdade das fichas.'}


if __name__ == '__main__':
    print(json.dumps(validar_pacote(), ensure_ascii=False, indent=2))
