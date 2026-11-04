"""Adaptação rank-1 de uma transformação linear 2x2, só com biblioteca padrão.

W0 é identidade e permanece congelada. A e B são treinados com escala alfa/r=1.
Não é treino de Transformer, LoRA de LLM, QLoRA ou benchmark de memória.
"""
import json
import math

BASE = ((1.0, 0.0), (0.0, 1.0))


def _numero(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x):
        raise ValueError("Esperado número real finito")
    return float(x)


def _vetor(x):
    v = tuple(_numero(n) for n in x)
    if len(v) != 2:
        raise ValueError("Esperado vetor de dimensão dois")
    return v


def _dados(pares):
    dados = [(_vetor(x), _vetor(y)) for x, y in pares]
    if not dados:
        raise ValueError("Sem dados")
    return dados


def _prever(x, a, b):
    h = sum(a[k] * x[k] for k in range(2))
    return tuple(sum(BASE[j][k] * x[k] for k in range(2)) + b[j] * h
                 for j in range(2))


def prever(x, a, b):
    return _prever(_vetor(x), _vetor(a), _vetor(b))


def perda_mse(pares, a, b):
    dados, a, b = _dados(pares), _vetor(a), _vetor(b)
    perda = sum((p - y[j]) ** 2 for x, y in dados
                for j, p in enumerate(_prever(x, a, b))) / (2 * len(dados))
    if not math.isfinite(perda):
        raise ValueError("Perda fora do intervalo numérico")
    return perda


def gradiente_mse(pares, a, b):
    dados, a, b = _dados(pares), _vetor(a), _vetor(b)
    da, db = [0.0, 0.0], [0.0, 0.0]
    for x, y in dados:
        h = sum(a[k] * x[k] for k in range(2))
        saida = _prever(x, a, b)
        d = [(saida[j] - y[j]) / len(dados) for j in range(2)]
        for j in range(2):
            db[j] += d[j] * h
        fator = sum(d[j] * b[j] for j in range(2))
        for k in range(2):
            da[k] += fator * x[k]
    return tuple(da), tuple(db)


def treinar_rank_um(pares, *, passos=1200, taxa=0.05):
    dados = _dados(pares)
    taxa = _numero(taxa)
    if type(passos) is not int or passos <= 0 or taxa <= 0:
        raise ValueError("Passos ou taxa inválidos")
    a, b = (0.1, -0.1), (0.0, 0.0)
    inicial = perda_mse(dados, a, b)
    for _ in range(passos):
        da, db = gradiente_mse(dados, a, b)
        # Atualização simultânea: os dois gradientes usam os mesmos pesos antigos.
        a = tuple(_numero(a[k] - taxa * da[k]) for k in range(2))
        b = tuple(_numero(b[j] - taxa * db[j]) for j in range(2))
    return {"base": BASE, "a": a, "b": b,
            "perda_inicial": inicial, "perda_final": perda_mse(dados, a, b)}


def demo():
    entradas = ((-1, 0), (1, 0), (0, -1), (0, 1))
    # Alvo W* = [[2, 2], [-1, -1]]; delta W* tem posto um.
    treino = [(x, (2 * x[0] + 2 * x[1], -x[0] - x[1])) for x in entradas]
    teste = [((1, 1), (4, -2)), ((-1, 2), (2, -1)), ((2, -1), (2, -1))]
    ajuste = treinar_rank_um(treino)
    impossivel = treinar_rank_um([(x, (2 * x[0], 2 * x[1])) for x in entradas])
    return {"tipo": "treino executado de adaptador rank-1 linear 2x2; dados sintéticos",
            "limite": "não é ajuste de LLM; não mede memória, linguagem ou hardware",
            "configuracao": {"passos": 1200, "taxa": 0.05, "alpha_div_r": 1,
                              "a_inicial": [0.1, -0.1], "b_inicial": [0.0, 0.0]},
            "treino": treino, "teste_reservado": teste, "ajuste": ajuste,
            "mse_teste": perda_mse(teste, ajuste["a"], ajuste["b"]),
            "delta_aprendido": [[ajuste["b"][j] * ajuste["a"][k] for k in range(2)] for j in range(2)],
            "alvo_delta_posto_dois": {"perda_inicial": impossivel["perda_inicial"],
                                       "perda_final": impossivel["perda_final"],
                                       "limite_inferior_neste_conjunto": 0.25}}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
