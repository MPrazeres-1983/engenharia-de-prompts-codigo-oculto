from fractions import Fraction
import math
import unittest

from exemplos.laboratorio.decisoes import (quadro_esperado, comparar_tempos,
    energia_constante, emissoes_estimadas)


class DecisoesTests(unittest.TestCase):
    def test_cenario_raro_com_oraculo_de_contagens(self):
        q = quadro_esperado(10000, 0.01, 0.9, 0.95)
        self.assertEqual((q.vp, q.fp, q.vn, q.fn), (90, 495, 9405, 10))
        self.assertEqual(q.metricas()["valor_preditivo_positivo"], Fraction(2, 13))
        self.assertEqual(q.vp + q.fp + q.vn + q.fn, 10000)

    def test_mudar_prevalencia_sem_mudar_taxas_condicionais(self):
        a = quadro_esperado(10000, 0.01, 0.9, 0.95)
        b = quadro_esperado(10000, 0.1, 0.9, 0.95)
        self.assertEqual((b.vp, b.fp, b.vn, b.fn), (900, 450, 8550, 100))
        self.assertEqual(b.metricas()["valor_preditivo_positivo"], Fraction(2, 3))
        for k in ("sensibilidade", "especificidade", "taxa_falsos_positivos"):
            self.assertEqual(a.metricas()[k], b.metricas()[k])

    def test_denominador_zero_nao_se_transforma_em_desempenho_perfeito(self):
        m = quadro_esperado(100, 0, 0.9, 1).metricas()
        self.assertIsNone(m["sensibilidade"])
        self.assertIsNone(m["valor_preditivo_positivo"])
        self.assertEqual(m["especificidade"], 1)
        self.assertIsNone(quadro_esperado(100, 1, 1, 0.9).metricas()["especificidade"])

    def test_valores_esperados_nao_sao_arredondados_como_observacoes(self):
        q = quadro_esperado(3, 0.5, 0.5, 0.5)
        self.assertEqual(q.vp, Fraction(3, 4))
        self.assertEqual(q.vp + q.fp + q.vn + q.fn, 3)

    def test_probabilidades_e_populacao_invalidas(self):
        for n in (0, -1, True, 1.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                quadro_esperado(n, 0.1, 0.9, 0.9)
        for p in (-0.1, 1.1, math.inf, math.nan, True, "0.1"):
            with self.subTest(p=p), self.assertRaises(ValueError):
                quadro_esperado(100, p, 0.9, 0.9)

    def test_metade_do_tempo_significa_dobro_da_producao_por_tempo(self):
        r = comparar_tempos(20, geracao=4, revisao=4, retrabalho=2)
        self.assertEqual(r["reducao_relativa_tempo"], Fraction(1, 2))
        self.assertEqual(r["variacao_relativa_producao_por_tempo"], 1)

    def test_revisao_e_retrabalho_podem_anular_rapidez_de_geracao(self):
        r = comparar_tempos(20, geracao=4, revisao=8, retrabalho=10)
        self.assertEqual(r["minutos_com_ia"], 22)
        self.assertEqual(r["reducao_relativa_tempo"], Fraction(-1, 10))
        self.assertEqual(r["variacao_relativa_producao_por_tempo"], Fraction(-1, 11))
        with self.assertRaises(ValueError):
            comparar_tempos(20, geracao=-1)
        with self.assertRaises(ValueError):
            comparar_tempos(0, geracao=1)

    def test_energia_tem_unidades_e_fronteiras_explicitas(self):
        self.assertEqual(energia_constante(100, Fraction(1, 6)), Fraction(1, 60))
        e = energia_constante(100, Fraction(1, 6), pue=1.2)
        self.assertEqual(e, Fraction(1, 50))
        self.assertEqual(emissoes_estimadas(e, 0.2), Fraction(1, 250))

    def test_limites_de_energia_e_fatores(self):
        self.assertEqual(energia_constante(0, 1), 0)
        for args in ((-1, 1), (1, -1), (True, 1), (math.inf, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                energia_constante(*args)
        with self.assertRaises(ValueError):
            energia_constante(100, 1, pue=0.9)
        with self.assertRaises(ValueError):
            emissoes_estimadas(1, -0.1)
