"""Confere integridade e reavalia a evidência guardada, sem executar um LLM."""

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from experiencias.llm_local.executar import casos  # noqa: E402
from exemplos.lavandaria.core import validar_saida  # noqa: E402


def verificar():
    pasta = Path(__file__).parent / "resultados/2026-11-03"
    manifesto = json.loads((pasta / "manifesto.json").read_text())
    for nome, campo in (("executar.py", "sha256_executor"),
                        ("resultados/2026-11-03/saidas.jsonl", "sha256_saidas")):
        atual = hashlib.sha256((Path(__file__).parent / nome).read_bytes()).hexdigest()
        if atual != manifesto[campo]:
            raise ValueError("Hash diferente: " + nome)
    registos = [json.loads(l) for l in (pasta / "saidas.jsonl").read_text().splitlines()]
    definicoes = {(f, v, i, seed): (m, schema, esperado, ctx)
                  for f, v, i, m, schema, esperado, ctx in casos() for seed in (42, 1337)}
    chaves = [(r["familia"], r["variante"], r["caso"], r["seed"]) for r in registos]
    if len(registos) != 52 or len(set(chaves)) != 52 or set(chaves) != set(definicoes):
        raise ValueError("Casos em falta, repetidos ou adicionais")
    grupos = defaultdict(lambda: defaultdict(int))
    for r, chave in zip(registos, chaves):
        mensagens, schema, esperado, contexto = definicoes[chave]
        pedido = r["request"]
        if (pedido["messages"] != mensagens or pedido["seed"] != r["seed"]
                or r["esperado"] != esperado or pedido["temperature"] != 0.2):
            raise ValueError("Pedido ou referência diferente dos casos predefinidos")
        if schema is not None and pedido.get("response_format") != {"type": "json_object", "schema": schema}:
            raise ValueError("Esquema diferente")
        escolha = r["response"]["choices"][0]
        if escolha["finish_reason"] != "stop" or "erro_execucao" in r:
            raise ValueError("Execução interrompida")
        texto = escolha["message"]["content"]
        metricas = {}
        if r["familia"] == "classificacao":
            metricas["correto"] = texto.strip() == esperado
        else:
            try:
                objeto = json.loads(texto)
                metricas["json_valido"] = True
            except ValueError:
                objeto = None
                metricas["json_valido"] = False
            if contexto is not None:
                try:
                    validar_saida(objeto, contexto)
                    metricas["contrato_valido"] = True
                except (ValueError, TypeError, KeyError):
                    metricas["contrato_valido"] = False
            else:
                valor = objeto.get("minutos") if type(objeto) is dict else "ausente"
                metricas["correto"] = (type(objeto) is dict and set(objeto) == {"minutos"}
                                       and (valor is None if esperado is None else
                                            type(valor) is int and valor == esperado))
        grupo = grupos[r["familia"] + "/" + r["variante"]]
        grupo["total"] += 1
        grupo["erros_execucao"] += 0
        for nome, valor in metricas.items():
            if r[nome] is not valor:
                raise ValueError("Métrica gravada não corresponde à resposta bruta")
            grupo[nome] += int(valor)
    resumo = {"total": len(registos), "grupos": dict(grupos)}
    if resumo != json.loads((pasta / "resumo.json").read_text()):
        raise ValueError("Resumo não corresponde às respostas")
    print(json.dumps({"registos_verificados": 52, "hashes": "ok", "metricas": "ok",
                      "nota": "Reavaliação da evidência; não é nova inferência nem revisão semântica."},
                     ensure_ascii=False))


if __name__ == "__main__":
    verificar()
