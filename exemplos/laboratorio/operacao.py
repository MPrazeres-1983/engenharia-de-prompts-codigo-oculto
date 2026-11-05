"""Reproduz um incidente sintético de cache e testa a recuperação local."""
from dataclasses import asdict, dataclass
import hashlib
import json
from pathlib import Path

ENSAIO = Path(__file__).resolve().parents[2] / "experiencias" / "operacao"


@dataclass(frozen=True)
class Politica:
    documento: str
    versao: str
    dias_uteis: int

    def proposta(self):
        dados = asdict(self)
        canonico = json.dumps(dados, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return {**dados, "sha256": hashlib.sha256(canonico).hexdigest()}


def carregar_politicas():
    dados = json.loads((ENSAIO / "politicas.json").read_text(encoding="utf-8"))
    return Politica(**dados["anterior"]), Politica(**dados["vigente"])


def consultar_cache(cache, vigente):
    return cache.setdefault((vigente.documento, vigente.versao), vigente)


def estrutura_valida(proposta):
    return (
        isinstance(proposta, dict)
        and proposta.keys() == {"documento", "versao", "dias_uteis", "sha256"}
        and all(isinstance(proposta[campo], str) and proposta[campo]
                for campo in ("documento", "versao", "sha256"))
        and len(proposta["sha256"]) == 64
        and all(c in "0123456789abcdef" for c in proposta["sha256"])
        and type(proposta["dias_uteis"]) is int and proposta["dias_uteis"] > 0
    )


def decidir(proposta, vigente):
    """A fonte vigente é obtida fora da cache que forneceu a proposta."""
    if not estrutura_valida(proposta):
        return {"estado": "encaminhado", "motivo": "estrutura_invalida"}
    esperado = vigente.proposta()
    if any(proposta[campo] != esperado[campo] for campo in ("documento", "versao", "sha256")):
        return {"estado": "encaminhado", "motivo": "fonte_desatualizada_ou_invalida"}
    if proposta["dias_uteis"] != vigente.dias_uteis:
        return {"estado": "encaminhado", "motivo": "prazo_incorreto"}
    return {"estado": "resposta_validada", "resposta": esperado}


def demo():
    anterior, vigente = carregar_politicas()
    cache_legada = {anterior.documento: anterior}
    obsoleta = cache_legada.setdefault(vigente.documento, vigente).proposta()
    cache_versionada = {(anterior.documento, anterior.versao): anterior}
    recuperada = consultar_cache(cache_versionada, vigente).proposta()
    return {
        "tipo": "incidente sintetico de cache",
        "chamadas_llm": 0,
        "politica_vigente": vigente.proposta(),
        "base": decidir(anterior.proposta(), anterior),
        "falha_injetada": {
            "proposta_da_sonda": obsoleta,
            "estrutura_valida": estrutura_valida(obsoleta),
            "decisao_do_canario": decidir(obsoleta, vigente),
        },
        "recuperacao": decidir(recuperada, vigente),
    }


if __name__ == "__main__":
    print(json.dumps(demo(), ensure_ascii=False, indent=2))
