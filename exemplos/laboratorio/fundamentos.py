"""Cálculos didáticos: não são treino de LLM, benchmark de GPU ou SDK de ML."""
import json
import math


def _finito(valor):
    if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not math.isfinite(valor):
        raise ValueError("Esperado número real finito")
    return float(valor)


def softmax(scores):
    valores = [_finito(v) for v in scores]
    if not valores:
        raise ValueError("Lista vazia")
    maior = max(valores)
    pesos = [math.exp(v - maior) for v in valores]
    total = sum(pesos)
    return [v / total for v in pesos]


def atencao_escalar(scores, valores):
    pesos = softmax(scores)
    dados = [_finito(v) for v in valores]
    if len(dados) != len(pesos):
        raise ValueError("Dimensões diferentes")
    return sum(p * v for p, v in zip(pesos, dados))


def xor_relu(a, b):
    """Pesos construídos à mão; demonstra representação, não treino."""
    if type(a) is not int or type(b) is not int or a not in (0, 1) or b not in (0, 1):
        raise ValueError("Esperados dois bits inteiros")
    h1 = max(0, a + b)
    h2 = max(0, a + b - 1)
    return h1 - 2 * h2


def retorno_descontado(recompensas, desconto):
    dados = [_finito(r) for r in recompensas]
    desconto = _finito(desconto)
    if not dados or not 0 <= desconto <= 1:
        raise ValueError("Episódio vazio ou desconto inválido")
    retorno = 0.0
    for recompensa in reversed(dados):
        retorno = recompensa + desconto * retorno
    if not math.isfinite(retorno):
        raise ValueError("Retorno fora do intervalo numérico")
    return retorno


def atualizar_q(valor, recompensa, melhor_seguinte, *, taxa, desconto, terminal=False):
    """Um passo tabular; não aprende uma política completa nem garante convergência."""
    valor, recompensa, seguinte, taxa, desconto = map(
        _finito, (valor, recompensa, melhor_seguinte, taxa, desconto))
    if type(terminal) is not bool or not 0 <= taxa <= 1 or not 0 <= desconto <= 1:
        raise ValueError("Taxa, desconto ou terminal inválido")
    alvo = recompensa + (0 if terminal else desconto * seguinte)
    novo = valor + taxa * (alvo - valor)
    if not math.isfinite(novo):
        raise ValueError("Atualização fora do intervalo numérico")
    return novo


def ajustar_reta(pontos, *, passos=1000, taxa=0.05):
    """Gradiente de MSE, sem normalização implícita ou mistura com o teste."""
    dados = [(_finito(x), _finito(y)) for x, y in pontos]
    taxa = _finito(taxa)
    if not dados or type(passos) is not int or passos < 1 or taxa <= 0:
        raise ValueError("Dados, passos ou taxa inválidos")
    peso = bias = 0.0
    for _ in range(passos):
        erros = [(x, peso * x + bias - y) for x, y in dados]
        peso -= taxa * 2 * sum(x * e for x, e in erros) / len(dados)
        bias -= taxa * 2 * sum(e for _, e in erros) / len(dados)
        if not math.isfinite(peso) or not math.isfinite(bias):
            raise ValueError("Treino divergiu; reduzir taxa ou reescalar dados")
    return peso, bias


def erro_quadratico(pontos, peso, bias):
    dados = [(_finito(x), _finito(y)) for x, y in pontos]
    if not dados:
        raise ValueError("Sem casos de avaliação")
    peso, bias = _finito(peso), _finito(bias)
    return sum((peso * x + bias - y) ** 2 for x, y in dados) / len(dados)


def quantizar_simetrico(valores, bits=4):
    """Grelha simétrica por tensor; sem empacotamento, treino ou formato GGUF."""
    dados = [_finito(v) for v in valores]
    if not dados or type(bits) is not int or not 2 <= bits <= 16:
        raise ValueError("Dados vazios ou bits fora de 2..16")
    limite = 2 ** (bits - 1) - 1
    escala = max(abs(v) for v in dados) / limite
    if escala == 0:
        return [0] * len(dados), 1.0, [0.0] * len(dados)
    inteiros = [max(-limite, min(limite, round(v / escala))) for v in dados]
    return inteiros, escala, [v * escala for v in inteiros]


def memoria_teorica(parametros, bits_pesos, *, camadas=0, cabecas_kv=0,
                    dimensao_cabeca=0, tokens=0, lote=1, bits_kv=16):
    """Bytes ideais dos pesos + KV denso; não estima toda a memória do runtime."""
    campos = [parametros, bits_pesos, camadas, cabecas_kv, dimensao_cabeca, tokens, lote, bits_kv]
    if any(type(v) is not int for v in campos):
        raise ValueError("Parâmetros inteiros, sem booleanos")
    if parametros < 1 or not 1 <= bits_pesos <= 64 or lote < 1 or not 1 <= bits_kv <= 64:
        raise ValueError("Parâmetros fora do intervalo")
    if min(camadas, cabecas_kv, dimensao_cabeca, tokens) < 0:
        raise ValueError("Dimensões negativas")
    pesos = (parametros * bits_pesos + 7) // 8
    kv_bits = 2 * camadas * cabecas_kv * dimensao_cabeca * tokens * lote * bits_kv
    return {"pesos_bytes": pesos, "kv_bytes": (kv_bits + 7) // 8,
            "exclui": ["escalas e metadados", "ativações", "buffers", "runtime", "otimizador"]}


def demo():
    treino = [(-1, -1), (0, 1), (1, 3)]
    teste = [(2, 5), (3, 7)]
    peso, bias = ajustar_reta(treino)
    _, escala, reconstruidos = quantizar_simetrico([-1.0, -0.3, 0.2, 1.0])
    return {"tipo": "cálculos executados, dados sintéticos; sem LLM",
            "reta": {"peso": peso, "bias": bias,
                     "mse_teste": erro_quadratico(teste, peso, bias)},
            "atencao": atencao_escalar([0, math.log(3)], [2, 6]),
            "xor_construido": [xor_relu(a, b) for a, b in ((0, 0), (0, 1), (1, 0), (1, 1))],
            "reforco": {"retorno": retorno_descontado([0, 0, 1], 0.9),
                         "q_passo": atualizar_q(0, 1, 2, taxa=0.5, desconto=0.9),
                         "q_terminal": atualizar_q(0, 1, 2, taxa=0.5, desconto=0.9, terminal=True)},
            "quantizacao": {"escala": escala, "reconstruidos": reconstruidos},
            "memoria": memoria_teorica(7_000_000_000, 4, camadas=32, cabecas_kv=8,
                                      dimensao_cabeca=128, tokens=4096)}


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
