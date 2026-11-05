"""Exporta o cartaz, a curta e o guião visual de A Meia Testemunha."""
import argparse
from fractions import Fraction
import hashlib
import importlib.metadata
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory
from xml.sax.saxutils import escape

from PIL import Image, ImageFont
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

RAIZ = Path(__file__).resolve().parent
FONTES = Path('/usr/share/fonts/truetype/dejavu')
NAVY = '#0b1726'
CREME = '#fff4df'
COBRE = '#ef9066'


def correr(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, text=True, check=True, capture_output=True).stdout


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validar_plano(plano, imagem, fonte):
    anterior = 0
    largura, altura = plano['largura'], plano['altura']
    if (largura, altura, plano['fps']) != (1280, 720, 24) or len(plano['planos']) != 3:
        raise ValueError('Este projeto usa três planos de 1280×720 a 24 fps')
    letra = ImageFont.truetype(str(fonte), 46)
    with Image.open(imagem) as arte:
        w, h = arte.size
    for plano_cena in plano['planos']:
        inicio, fim = plano_cena['inicio_s'], plano_cena['fim_s']
        if inicio != anterior or fim - inicio != 5:
            raise ValueError('Planos devem cobrir três intervalos contíguos de cinco segundos')
        anterior = fim
        cw, ch, x, y = plano_cena['recorte']
        if min(cw, ch) <= 0 or min(x, y) < 0 or x + cw > w or y + ch > h:
            raise ValueError('Enquadramento fora da ilustração')
        if cw * altura != ch * largura or not 0 <= plano_cena['zoom'] <= 0.1:
            raise ValueError('Proporções ou zoom fora do plano de montagem')
        if letra.getlength(plano_cena['legenda']) > largura - 128:
            raise ValueError('Intertítulo demasiado largo')
    return w, h


def exportar_video(pasta, imagem, plano, serif, sans):
    shutil.copyfile(serif, pasta / 'titulo.ttf')
    shutil.copyfile(sans, pasta / 'selo.ttf')
    filtros = ['[0:v]split=3[i0][i1][i2]']
    for i, cena in enumerate(plano['planos']):
        (pasta / f'legenda{i}.txt').write_text(cena['legenda'], encoding='utf-8')
        (pasta / f'selo{i}.txt').write_text(cena['selo'], encoding='utf-8')
        w, h, x, y = cena['recorte']
        zoom = cena['zoom']
        filtros.append(
            f'[i{i}]crop={w}:{h}:{x}:{y},'
            f"zoompan=z='1+{zoom}*on/119':x='iw/2-iw/zoom/2':"
            "y='ih/2-ih/zoom/2':d=120:s=1280x720:fps=24,"
            'setsar=1,format=yuv420p,setpts=PTS-STARTPTS,'
            'drawbox=x=0:y=584:w=iw:h=136:color=0x0b1726@0.97:t=fill,'
            'drawbox=x=64:y=612:w=28:h=4:color=0xef9066:t=fill,'
            f'drawtext=fontfile=selo.ttf:textfile=selo{i}.txt:expansion=none:'
            'x=108:y=602:fontsize=19:fontcolor=0xef9066,'
            f'drawtext=fontfile=titulo.ttf:textfile=legenda{i}.txt:expansion=none:'
            f'x=64:y=640:fontsize=46:fontcolor=0xfff4df[o{i}]'
        )
    filtros.append('[o0][o1][o2]concat=n=3:v=1:a=0[saida]')
    saida = pasta / 'curta.mp4'
    correr('ffmpeg', '-nostdin', '-v', 'error', '-i', str(imagem),
           '-filter_complex_threads', '1', '-filter_complex', ';'.join(filtros),
           '-map', '[saida]', '-an', '-c:v', 'libx264', '-preset', 'medium',
           '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
           '-metadata', 'title=A Meia Testemunha', str(saida), cwd=pasta)
    return saida


def verificar_video(path):
    info = json.loads(correr('ffprobe', '-v', 'error', '-count_frames',
                             '-show_streams', '-show_format', '-of', 'json', str(path)))
    (video,) = info['streams']
    observado = {
        'codec': video['codec_name'],
        'largura': video['width'],
        'altura': video['height'],
        'fps': int(Fraction(video['r_frame_rate'])),
        'fotogramas': int(video['nb_read_frames']),
        'duracao_s': float(info['format']['duration']),
        'audio': False,
    }
    if (video['codec_type'] != 'video' or Fraction(video['r_frame_rate']) != 24
            or observado != {'codec': 'h264', 'largura': 1280, 'altura': 720,
                              'fps': 24, 'fotogramas': 360, 'duracao_s': 15.0,
                              'audio': False}):
        raise ValueError(f'Exportação fora do plano: {observado}')
    return observado


def exportar_guiao(pasta, video, plano, sans, regular):
    pdfmetrics.registerFont(TTFont('GuiaoRegular', str(regular)))
    pdfmetrics.registerFont(TTFont('GuiaoNegrito', str(sans)))
    folha = pasta / 'guiao_visual.pdf'
    largura, altura = A4
    pdf = canvas.Canvas(str(folha), pagesize=A4, invariant=True)
    pdf.setTitle('A Meia Testemunha — guião visual')
    pdf.setAuthor('Mário Prazeres')
    pdf.setFillColor(HexColor(NAVY))
    pdf.rect(0, 0, largura, altura, stroke=0, fill=1)
    pdf.setFillColor(HexColor(COBRE))
    pdf.setFont('GuiaoNegrito', 10)
    pdf.drawString(42, 801, 'ESTÚDIO DA LAVANDARIA   /   FICÇÃO')
    pdf.setFillColor(HexColor(CREME))
    pdf.setFont('GuiaoNegrito', 27)
    pdf.drawString(42, 765, 'A MEIA TESTEMUNHA')
    pdf.setFont('GuiaoRegular', 11)
    pdf.drawString(42, 740, 'Guião visual com fotogramas da curta exportada')
    titulo = ParagraphStyle('intertitulo', fontName='GuiaoNegrito', fontSize=15,
                            leading=18, textColor=HexColor(CREME))
    nota = ParagraphStyle('observacao', fontName='GuiaoRegular', fontSize=10.5,
                          leading=14, textColor=HexColor('#c2d0df'))
    for i, cena in enumerate(plano['planos']):
        meio = (cena['inicio_s'] + cena['fim_s']) / 2
        frame = pasta / f'frame{i}.jpg'
        correr('ffmpeg', '-nostdin', '-v', 'error', '-ss', str(meio), '-i', str(video),
               '-frames:v', '1', '-q:v', '3', str(frame))
        topo = 707 - i * 181
        pdf.drawImage(str(frame), 42, topo - 146.25, 260, 146.25)
        pdf.setFillColor(HexColor(COBRE))
        pdf.setFont('GuiaoNegrito', 10)
        pdf.drawString(322, topo - 11, f"{cena['selo']}   ·   {cena['inicio_s']}–{cena['fim_s']} s")
        paragrafo = Paragraph(escape(cena['legenda']), titulo)
        _, h_titulo = paragrafo.wrap(230, 95)
        paragrafo.drawOn(pdf, 322, topo - 28 - h_titulo)
        paragrafo = Paragraph(escape(cena['observacao']), nota)
        _, h_nota = paragrafo.wrap(230, 95)
        if 39 + h_titulo + h_nota > 146.25:
            raise ValueError('Texto de plano fora da zona do guião')
        paragrafo.drawOn(pdf, 322, topo - 39 - h_titulo - h_nota)
    pdf.setStrokeColor(HexColor('#546476'))
    pdf.line(42, 151, largura - 42, 151)
    pdf.setFillColor(HexColor('#c2d0df'))
    pdf.setFont('GuiaoRegular', 10)
    pdf.drawString(42, 127, 'Amostras a 2,5 s, 7,5 s e 12,5 s. Intertítulos visíveis. Curta muda.')
    pdf.drawString(42, 105, 'Ilustração gerada para o projeto. Enquadramento, texto e montagem definidos no guião.')
    pdf.setFillColor(HexColor(CREME))
    pdf.setFont('GuiaoNegrito', 11)
    pdf.drawString(42, 65, 'Mário Prazeres  ·  O Código Oculto da Inteligência Artificial')
    pdf.showPage()
    pdf.save()
    return folha


def montar(destino, fontes_tipograficas):
    destino = destino.resolve()
    if destino.exists():
        raise FileExistsError(f'Escolhe uma pasta nova: {destino}')
    destino.parent.mkdir(parents=True, exist_ok=True)
    plano_path = RAIZ / 'plano.json'
    plano = json.loads(plano_path.read_text(encoding='utf-8'))
    imagem = RAIZ / plano['imagem']
    serif = fontes_tipograficas / 'DejaVuSerif-Bold.ttf'
    sans = fontes_tipograficas / 'DejaVuSans-Bold.ttf'
    regular = fontes_tipograficas / 'DejaVuSans.ttf'
    dimensoes = validar_plano(plano, imagem, serif)
    with TemporaryDirectory(prefix='.atelier-', dir=destino.parent) as temp:
        pasta = Path(temp)
        cartaz = pasta / 'cartaz.pdf'
        correr('inkscape', str(RAIZ / 'cartaz.svg'), '--export-type=pdf',
               f'--export-filename={cartaz}')
        video = exportar_video(pasta, imagem, plano, serif, sans)
        observado = verificar_video(video)
        guiao = exportar_guiao(pasta, video, plano, sans, regular)
        artefactos = [cartaz, video, guiao]
        fontes = [imagem, plano_path, RAIZ / 'cartaz.svg', Path(__file__).resolve()]
        resultado = {
            'projeto': plano['titulo'],
            'tipo': 'ficção e montagem de uma ilustração gerada',
            'imagem_dimensoes': list(dimensoes),
            'fontes_sha256': {p.name: sha256(p) for p in fontes},
            'tipografia_sha256': {p.name: sha256(p) for p in (serif, sans, regular)},
            'video_verificado': observado,
            'amostras_s': [2.5, 7.5, 12.5],
            'artefactos': {p.name: {'sha256': sha256(p), 'bytes': p.stat().st_size}
                          for p in artefactos},
            'ambiente': {'ffmpeg': correr('ffmpeg', '-version').splitlines()[0],
                         'inkscape': correr('inkscape', '--version').strip(),
                         'reportlab': importlib.metadata.version('reportlab')},
        }
        entrega = pasta / 'entrega'
        entrega.mkdir()
        for p in artefactos:
            p.rename(entrega / p.name)
        (entrega / 'resultado.json').write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + '\n',
                                               encoding='utf-8')
        entrega.rename(destino)
    return resultado


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destino', type=Path, default=Path('build/atelier'))
    parser.add_argument('--fontes', type=Path, default=FONTES)
    args = parser.parse_args()
    try:
        print(json.dumps(montar(args.destino, args.fontes.resolve()), ensure_ascii=False, indent=2))
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.stderr.strip() or f'Falha na execução de {exc.cmd[0]}') from exc
