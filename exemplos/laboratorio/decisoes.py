"""Contas didáticas de decisão: pressupostos sintéticos, não resultados clínicos.

As frações evitam arredondar valores esperados como se fossem pessoas observadas.
O módulo não ajusta modelos, estima probabilidades ou mede energia de hardware.
"""
from dataclasses import dataclass
from fractions import Fraction
import json
import math


def _fracao(valor):
    if isinstance(valor, bool) or not isinstance(valor, (int, float, Fraction)):
        raise ValueError("Esperado número, sem booleanos")
    if isinstance(valor, float) and not math.isfinite(valor):
        raise ValueError("Esperado número finito")
    return valor if isinstance(valor, Fraction) else Fraction(str(valor))


def _probabilidade(valor):
    valor = _fracao(valor)
    if not 0 <= valor <= 1:
        raise ValueError("Probabilidade fora de 0..1")
    return valor


def _nao_negativo(valor):
    valor = _fracao(valor)
    if valor < 0:
        raise ValueError("Valor negativo")
    return valor


def _dividir(numerador, denominador):
    return numerador / denominador if denominador else None


@dataclass(frozen=True)
class QuadroEsperado:
    """Contagens esperadas, que podem ser fracionárias; não são uma amostra."""
    vp: Fraction
    fp: Fraction
    vn: Fraction
    fn: Fraction

    def metricas(self):
        return {
            "sensibilidade": _dividir(self.vp, self.vp + self.fn),
            "especificidade": _dividir(self.vn, self.vn + self.fp),
            "valor_preditivo_positivo": _dividir(self.vp, self.vp + self.fp),
            "taxa_falsos_positivos": _dividir(self.fp, self.fp + self.vn),
        }


def quadro_esperado(populacao, prevalencia, sensibilidade, especificidade):
    if type(populacao) is not int or populacao <= 0:
        raise ValueError("População deve ser um inteiro positivo")
    p, s, e = map(_probabilidade, (prevalencia, sensibilidade, especificidade))
    positivos = populacao * p
    negativos = populacao * (1 - p)
    return QuadroEsperado(positivos * s, negativos * (1 - e),
                         negativos * e, positivos * (1 - s))


def comparar_tempos(minutos_sem_ia, *, preparacao=0, geracao=0, revisao=0,
                    retrabalho=0):
    """Mesma quantidade e qualidade de tarefas aceites; tempos completos dados."""
    base = _nao_negativo(minutos_sem_ia)
    total = sum(map(_nao_negativo, (preparacao, geracao, revisao, retrabalho)))
    if base == 0 or total == 0:
        raise ValueError("Tempos totais devem ser positivos")
    return {"minutos_sem_ia": base, "minutos_com_ia": total,
            "reducao_relativa_tempo": 1 - total / base,
            "variacao_relativa_producao_por_tempo": base / total - 1}


def energia_constante(potencia_it_w, duracao_h, *, pue=1):
    """kWh sob potência constante e fronteira explícita; não faz telemetria."""
    potencia = _nao_negativo(potencia_it_w)
    duracao = _nao_negativo(duracao_h)
    pue = _fracao(pue)
    if pue < 1:
        raise ValueError("PUE deve ser pelo menos 1 para esta fronteira")
    return potencia * duracao * pue / 1000


def emissoes_estimadas(energia_kwh, fator_kg_por_kwh):
    """kg CO2e com fator fornecido; não inclui fabrico ou água."""
    return _nao_negativo(energia_kwh) * _nao_negativo(fator_kg_por_kwh)


def _json(valor):
    if isinstance(valor, Fraction):
        return {"fracao": str(valor), "aproximacao": float(valor)}
    if isinstance(valor, dict):
        return {k: _json(v) for k, v in valor.items()}
    return valor


def demo():
    raro = quadro_esperado(10000, Fraction(1, 100), Fraction(9, 10), Fraction(95, 100))
    frequente = quadro_esperado(10000, Fraction(1, 10), Fraction(9, 10), Fraction(95, 100))
    energia = energia_constante(100, Fraction(1, 6), pue=Fraction(6, 5))
    return _json({
        "tipo": "cálculos executados com pressupostos sintéticos; sem LLM ou pessoas",
        "prevalencia_1_por_cento": {"contagens": raro.__dict__, "metricas": raro.metricas()},
        "prevalencia_10_por_cento": {"contagens": frequente.__dict__, "metricas": frequente.metricas()},
        "rapidez_20_para_10_min": comparar_tempos(20, geracao=4, revisao=4, retrabalho=2),
        "rapidez_20_para_22_min": comparar_tempos(20, geracao=4, revisao=8, retrabalho=10),
        "energia_kwh_construida": energia,
        "emissoes_kg_construidas": emissoes_estimadas(energia, Fraction(1, 5)),
        "exclui": "dados reais de saúde, medição elétrica, água, fabrico e treino de modelo",
    })


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
