"""Regressão determinística. Não é conjunto reservado nem benchmark de um LLM."""
import json
import math
from .core import BASE, responder


def wilson(acertos: int, total: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if type(acertos) is not int or type(total) is not int or total <= 0 or not 0 <= acertos <= total:
        raise ValueError("Contagens inválidas")
    if not math.isfinite(z) or z <= 0:
        raise ValueError("z deve ser finito e positivo")
    p = acertos / total
    denominador = 1 + z*z/total
    centro = (p + z*z/(2*total)) / denominador
    raio = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total)) / denominador
    return max(0., centro-raio), min(1., centro+raio)


def avaliar() -> dict:
    casos = json.loads((BASE / "dados/casos_avaliacao.json").read_text(encoding="utf-8"))
    resultados = []
    for caso in casos:
        resposta = responder(caso["pedido"], caso["cliente"])
        fontes = [e["fonte"] for e in resposta["evidencias"]]
        correto = (resposta["categoria"] == caso["categoria"]
                   and resposta["precisa_humano"] == caso["humano"]
                   and fontes == ([caso["fonte"]] if caso["fonte"] else []))
        resultados.append({"id": caso["id"], "passou": correto})
    return {"modo": "regressao_offline_templates_sem_LLM", "total": len(casos),
            "passaram": sum(r["passou"] for r in resultados), "casos": resultados,
            "nota": "Casos conhecidos de regressão; sem estimativa de generalização ou desempenho de um modelo.",
            "wilson_exemplo_8_em_10": list(wilson(8, 10))}


if __name__ == "__main__":
    resultado = avaliar()
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    raise SystemExit(0 if resultado["passaram"] == resultado["total"] else 1)
