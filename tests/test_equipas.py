import threading
import unittest
from exemplos.laboratorio.equipas import ClienteLocal, Orcamento, executar, stub


class EquipasTests(unittest.TestCase):
    def test_um_ou_tres_passos_sem_confundir_stub_com_llm(self):
        for modo, n in [('unico', 1), ('equipa', 3)]:
            r = executar('Faltam duas meias.', stub, modo=modo)
            self.assertEqual((r['estado'], r['chamadas']), ('concluido', n))
            self.assertEqual(r['saida'], {'categoria': 'pecas_em_falta', 'fonte': 'POL-01'})

    def test_orcamento_impede_sintese_apos_dois_workers(self):
        r = executar('Faltam meias.', stub, limite=2)
        self.assertEqual(r['estado'], 'encaminhar')
        self.assertIsNone(r['saida'])
        self.assertEqual(r['chamadas'], 2)

    def test_falha_parcial_nao_e_sucesso(self):
        def falha(papel, *args):
            if papel == 'documental':
                raise TimeoutError('Falha sintética')
            return {'categoria': 'outro', 'fonte': None}
        self.assertEqual(executar('Pedido', falha)['estado'], 'encaminhar')

    def test_campo_extra_nao_atravessa_o_contrato(self):
        def invalido(*args):
            return {'categoria': 'outro', 'fonte': None, 'executar': 'comando proibido'}
        self.assertEqual(executar('Pedido', invalido, modo='unico')['estado'], 'encaminhar')

    def test_workers_recebem_mesmo_snapshot_e_sintese_recebe_propostas(self):
        vistos = []
        lock = threading.Lock()
        def adaptador(papel, pedido, contexto, seed):
            with lock:
                vistos.append((papel, contexto))
            return {'categoria': 'outro', 'fonte': None}
        self.assertEqual(executar('Pedido', adaptador)['estado'], 'concluido')
        d = dict(vistos)
        self.assertEqual(d['triagem'], d['documental'])
        self.assertIn('propostas_nao_autoritativas', d['supervisor'])

    def test_reserva_concorrente_nao_excede_limite(self):
        orcamento = Orcamento(1)
        resultados = []
        def tentar():
            try:
                orcamento.reservar()
                resultados.append(True)
            except RuntimeError:
                resultados.append(False)
        a, b = threading.Thread(target=tentar), threading.Thread(target=tentar)
        a.start(); b.start(); a.join(); b.join()
        self.assertEqual(sum(resultados), 1)
        self.assertEqual(orcamento.usados, 1)

    def test_rede_externa_e_credenciais_na_url_nao_sao_aceites(self):
        for url in ('https://example.com', 'http://example.com', 'http://user:pass@localhost',
                    'http://localhost/segredo', 'http://127.0.0.1?x=1'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                ClienteLocal(url, 'modelo')

    def test_pedido_vazio_e_modo_desconhecido(self):
        with self.assertRaises(ValueError):
            executar('', stub)
        with self.assertRaises(ValueError):
            executar('Pedido', stub, modo='inexistente')
