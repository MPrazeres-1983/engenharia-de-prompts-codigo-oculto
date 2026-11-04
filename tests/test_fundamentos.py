import math
import unittest
from exemplos.laboratorio.fundamentos import (softmax, atencao_escalar, ajustar_reta,
    erro_quadratico, quantizar_simetrico, memoria_teorica, xor_relu,
    retorno_descontado, atualizar_q)


class FundamentosTests(unittest.TestCase):
    def test_xor_tabela_completa_e_pesos_construidos(self):
        self.assertEqual([xor_relu(a, b) for a, b in ((0, 0), (0, 1), (1, 0), (1, 1))],
                         [0, 1, 1, 0])
        with self.assertRaises(ValueError):
            xor_relu(True, 0)

    def test_retornos_com_desconto_e_sem_futuro(self):
        self.assertAlmostEqual(retorno_descontado([0, 0, 1], 0.9), 0.81)
        self.assertEqual(retorno_descontado([1, 2, 3], 0), 1)
        self.assertEqual(retorno_descontado([1, 2, 3], 1), 6)

    def test_q_terminal_nao_transporta_valor_de_outra_jogada(self):
        self.assertAlmostEqual(atualizar_q(0, 1, 2, taxa=0.5, desconto=0.9), 1.4)
        self.assertEqual(atualizar_q(0, 1, 2, taxa=0.5, desconto=0.9, terminal=True), 0.5)

    def test_reforco_rejeita_estado_de_calculo_invalido(self):
        for recompensas, desconto in (([], 0.9), ([1], -0.1), ([math.inf], 0.9)):
            with self.subTest(recompensas=recompensas), self.assertRaises(ValueError):
                retorno_descontado(recompensas, desconto)
        with self.assertRaises(ValueError):
            atualizar_q(0, 1, 2, taxa=1.1, desconto=0.9)
        with self.assertRaises(ValueError):
            atualizar_q(0, 1, 2, taxa=0.5, desconto=0.9, terminal=1)

    def test_atencao_exemplo_do_manuscrito(self):
        self.assertAlmostEqual(atencao_escalar([0, math.log(3)], [2, 6]), 5)

    def test_softmax_resiste_a_scores_grandes_e_translacao(self):
        self.assertEqual(softmax([1000, 1000]), [0.5, 0.5])
        for a, b in zip(softmax([1, 2]), softmax([1001, 1002])):
            self.assertAlmostEqual(a, b)

    def test_rejeita_dados_nao_finitos_e_dimensoes_erradas(self):
        for dados in ([], [math.nan], [math.inf], [True]):
            with self.subTest(dados=dados), self.assertRaises(ValueError):
                softmax(dados)
        with self.assertRaises(ValueError):
            atencao_escalar([0, 1], [2])

    def test_gradiente_recupera_reta_e_extrapola_em_teste_reservado(self):
        peso, bias = ajustar_reta([(-1, -1), (0, 1), (1, 3)])
        self.assertAlmostEqual(peso, 2, places=6)
        self.assertAlmostEqual(bias, 1, places=6)
        self.assertLess(erro_quadratico([(2, 5), (3, 7)], peso, bias), 1e-10)

    def test_treino_e_avaliacao_invalidos(self):
        with self.assertRaises(ValueError):
            ajustar_reta([], passos=1)
        with self.assertRaises(ValueError):
            ajustar_reta([(1, 2)], taxa=-1)
        with self.assertRaises(ValueError):
            erro_quadratico([], 1, 0)

    def test_quantizacao_limite_de_erro_e_zero(self):
        dados = [-1, -0.3, 0.2, 1]
        _, escala, saida = quantizar_simetrico(dados, 4)
        self.assertTrue(all(abs(a-b) <= escala/2+1e-12 for a,b in zip(dados, saida)))
        self.assertEqual(quantizar_simetrico([0, 0])[2], [0, 0])
        with self.assertRaises(ValueError):
            quantizar_simetrico(dados, 1)

    def test_memoria_pesos_e_kv_sao_distintos(self):
        r = memoria_teorica(7_000_000_000, 4, camadas=32, cabecas_kv=8,
                            dimensao_cabeca=128, tokens=4096)
        self.assertEqual(r['pesos_bytes'], 3_500_000_000)
        self.assertEqual(r['kv_bytes'], 536_870_912)
        self.assertEqual(memoria_teorica(1, 1)['pesos_bytes'], 1)

    def test_memoria_rejeita_dimensoes_negativas_e_booleanos(self):
        with self.assertRaises(ValueError):
            memoria_teorica(100, 4, tokens=-1)
        with self.assertRaises(ValueError):
            memoria_teorica(True, 4)
