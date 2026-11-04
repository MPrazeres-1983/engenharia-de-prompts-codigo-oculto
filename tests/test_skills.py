import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest
from exemplos.laboratorio.skills import PACOTE, validar_pacote

validar = runpy.run_path(str(PACOTE/'scripts/validar_fichas.py'))['validar']


class SkillsTests(unittest.TestCase):
    def test_pacote_e_fichas_validos(self):
        self.assertEqual(validar_pacote()['hashes'], 'ok')
        self.assertEqual(validar(json.loads((PACOTE/'assets/fichas.json').read_text()))['fichas'], 2)

    def test_estrutura_nao_equivale_a_verdade(self):
        ficha = {'afirmacao': 'A Lua é feita de meias.', 'fonte': 'Fonte fictícia',
                 'localizador': 'p. 1', 'alcance': 'Ficção', 'estado': 'suportada'}
        self.assertEqual(validar([ficha])['factos'], 'nao verificados pelo script')

    def test_conclusao_sem_localizador_e_rejeitada(self):
        ficha = {'afirmacao': 'Uma afirmação', 'fonte': 'Fonte', 'localizador': '',
                 'alcance': 'Limitado', 'estado': 'suportada'}
        with self.assertRaises(ValueError):
            validar([ficha])

    def test_campo_extra_e_tipo_errado(self):
        for obj in ([{'afirmacao': 'x'}], [], {'afirmacao': 'x'}):
            with self.subTest(obj=obj), self.assertRaises(ValueError):
                validar(obj)

    def test_alteracao_de_script_e_detetada(self):
        with tempfile.TemporaryDirectory() as tmp:
            copia = Path(tmp)/PACOTE.name
            shutil.copytree(PACOTE, copia)
            (copia/'scripts/validar_fichas.py').write_text('print("alterado")')
            with self.assertRaisesRegex(ValueError, 'Hash'):
                validar_pacote(copia)

    def test_manifesto_nao_pode_ler_fora_do_pacote(self):
        with tempfile.TemporaryDirectory() as tmp:
            copia = Path(tmp)/PACOTE.name
            shutil.copytree(PACOTE, copia)
            (Path(tmp)/'externo.txt').write_text('fictício')
            manifesto = json.loads((copia/'manifesto.json').read_text())
            manifesto['ficheiros'] = {'../externo.txt': '0'*64}
            (copia/'manifesto.json').write_text(json.dumps(manifesto))
            with self.assertRaisesRegex(ValueError, 'fora'):
                validar_pacote(copia)
