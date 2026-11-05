import math
import unittest
from exemplos.laboratorio.adaptacao import (BASE, prever, perda_mse,
    gradiente_mse, treinar_rank_um)


class AdaptacaoTests(unittest.TestCase):
    def setUp(self):
        self.entradas = ((-1, 0), (1, 0), (0, -1), (0, 1))
        self.treino = [(x, (2*x[0]+2*x[1], -x[0]-x[1])) for x in self.entradas]

    def test_base_sem_adaptador_e_conservacao_dos_pesos(self):
        original = tuple(tuple(linha) for linha in BASE)
        self.assertEqual(prever((2, -3), (0.1, 0.2), (0, 0)), (2, -3))
        ajuste = treinar_rank_um(self.treino)
        self.assertEqual(BASE, original)
        self.assertEqual(ajuste["base"], original)

    def test_gradiente_com_oraculo_numerico_independente(self):
        a, b, eps = [0.2, -0.3], [0.4, -0.1], 1e-6
        ga, gb = gradiente_mse(self.treino, a, b)
        for grupo, analitico in ((0, ga), (1, gb)):
            for k in range(2):
                mais, menos = [a.copy(), b.copy()], [a.copy(), b.copy()]
                mais[grupo][k] += eps
                menos[grupo][k] -= eps
                numerico = (perda_mse(self.treino, *mais)-perda_mse(self.treino, *menos))/(2*eps)
                self.assertAlmostEqual(analitico[k], numerico, places=7)

    def test_treino_aprende_delta_rank_um_e_casos_nao_usados(self):
        ajuste = treinar_rank_um(self.treino)
        self.assertLess(ajuste["perda_final"], 1e-12)
        for x, y in (((1, 1), (4, -2)), ((-1, 2), (2, -1)), ((2, -1), (2, -1))):
            self.assertLess(sum((a-b)**2 for a,b in zip(prever(x, ajuste["a"], ajuste["b"]), y)), 1e-10)
        a, b = ajuste["a"], ajuste["b"]
        self.assertAlmostEqual((b[0]*a[0])*(b[1]*a[1])-(b[0]*a[1])*(b[1]*a[0]), 0)

    def test_posto_um_nao_representa_delta_identidade_de_posto_dois(self):
        ajuste = treinar_rank_um([(x, (2*x[0], 2*x[1])) for x in self.entradas])
        self.assertGreaterEqual(ajuste["perda_final"], 0.25-1e-12)
        self.assertLess(ajuste["perda_final"], 0.250001)

    def test_rejeita_dados_ou_configuracao_invalidos(self):
        for dados in ([], [((1,), (1, 2))], [((1, math.nan), (1, 2))]):
            with self.subTest(dados=dados), self.assertRaises(ValueError):
                treinar_rank_um(dados)
        for opcoes in ({"passos": True}, {"passos": 0}, {"taxa": -1}):
            with self.subTest(opcoes=opcoes), self.assertRaises(ValueError):
                treinar_rank_um(self.treino, **opcoes)
