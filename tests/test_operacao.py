import json
import unittest

from exemplos.laboratorio.operacao import (
    ENSAIO, Politica, carregar_politicas, consultar_cache, decidir, demo, estrutura_valida,
)


class OperacaoTests(unittest.TestCase):
    def setUp(self):
        self.anterior, self.vigente = carregar_politicas()

    def test_forma_valida_com_fonte_antiga_e_encaminhada_sem_prazo(self):
        antiga = self.anterior.proposta()
        self.assertTrue(estrutura_valida(antiga))
        self.assertEqual(decidir(antiga, self.vigente), {
            "estado": "encaminhado", "motivo": "fonte_desatualizada_ou_invalida",
        })

    def test_cache_versionada_recupera_prazo_vigente_com_entrada_antiga(self):
        cache = {(self.anterior.documento, self.anterior.versao): self.anterior}
        nova = consultar_cache(cache, self.vigente)
        self.assertEqual(len(cache), 2)
        self.assertEqual(cache[("devolucoes", "v1")].dias_uteis, 10)
        self.assertEqual(decidir(nova.proposta(), self.vigente), {
            "estado": "resposta_validada", "resposta": self.vigente.proposta(),
        })
        self.assertEqual(nova.dias_uteis, 5)

    def test_versao_correta_com_conteudo_adulterado_e_encaminhada(self):
        alterada = Politica(self.vigente.documento, self.vigente.versao, 11)
        self.assertNotEqual(alterada.proposta()["sha256"], self.vigente.proposta()["sha256"])
        self.assertEqual(decidir(alterada.proposta(), self.vigente)["motivo"],
                         "fonte_desatualizada_ou_invalida")

    def test_hash_de_origem_correto_com_prazo_errado_e_encaminhado(self):
        proposta = {**self.vigente.proposta(), "dias_uteis": 10}
        self.assertEqual(decidir(proposta, self.vigente), {
            "estado": "encaminhado", "motivo": "prazo_incorreto",
        })

    def test_estrutura_invalida_e_encaminhada(self):
        for proposta in (None, {}, {**self.vigente.proposta(), "dias_uteis": True}):
            with self.subTest(proposta=proposta):
                self.assertEqual(decidir(proposta, self.vigente), {
                    "estado": "encaminhado", "motivo": "estrutura_invalida",
                })

    def test_registo_de_execucao_reproduzivel(self):
        gravado = json.loads((ENSAIO / "resultado.json").read_text(encoding="utf-8"))
        self.assertEqual(demo(), gravado)
        self.assertEqual(gravado["chamadas_llm"], 0)
