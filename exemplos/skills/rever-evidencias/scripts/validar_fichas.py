"""Validação estrutural de um contrato específico; não verifica factos ou URLs."""
import json
import sys

CAMPOS = {"afirmacao", "fonte", "localizador", "alcance", "estado"}
ESTADOS = {"suportada", "nao_suportada", "por_verificar"}


def validar(fichas):
    if type(fichas) is not list or not fichas:
        raise ValueError("Esperada lista não vazia")
    for i, ficha in enumerate(fichas):
        if type(ficha) is not dict or set(ficha) != CAMPOS:
            raise ValueError(f"Ficha {i}: campos em falta ou extra")
        if any(type(v) is not str for v in ficha.values()):
            raise ValueError(f"Ficha {i}: valores devem ser strings")
        if not ficha['afirmacao'].strip() or ficha['estado'] not in ESTADOS:
            raise ValueError(f"Ficha {i}: afirmação ou estado inválido")
        if ficha['estado'] != 'por_verificar' and any(
                not ficha[c].strip() for c in ('fonte', 'localizador', 'alcance')):
            raise ValueError(f"Ficha {i}: conclusão sem localização/alcance")
    return {"fichas": len(fichas), "estrutura": "valida", "factos": "nao verificados pelo script"}


if __name__ == '__main__':
    try:
        # Limite em caracteres, adequado ao pequeno exercício; não é um serviço público.
        texto = sys.stdin.read(100_001)
        if len(texto) > 100_000:
            raise ValueError("Entrada excede 100000 caracteres")
        print(json.dumps(validar(json.loads(texto)), ensure_ascii=False))
    except (ValueError, TypeError) as erro:
        print(json.dumps({"erro": str(erro)}, ensure_ascii=False), file=sys.stderr)
        sys.exit(1)
