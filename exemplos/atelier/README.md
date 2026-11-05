# A Meia Testemunha

## A cena

O gerente da Lavandaria encontrou uma meia vermelha no balcão. Abriu a máquina, fechou-a e voltou a abri-la, para dar ao suspeito a oportunidade de mudar de versão. Pelo vidro via-se o tambor vazio. No cesto de vime, mesmo ao lado, uma faixa clara interrompia o desenho do rebordo. A outra meia tinha ficado presa por fora. O gerente riscou «interrogar máquina» da lista e escreveu «olhar para o cesto». Era uma instrução mais curta. Também era a primeira que tinha seguido até ao fim.

Ficção original da Lavandaria das Meias Desaparecidas, no livro de Mário Prazeres. O cartaz dá ao leitor a imagem inteira. A curta guarda o cesto para o último enquadramento.

## Ficheiros

| Ficheiro | Conteúdo |
|---|---|
| [ilustracao.png](ilustracao.png) | Arte de origem a 1672 × 941 píxeis |
| [cartaz.svg](cartaz.svg) e [cartaz.pdf](saidas/cartaz.pdf) | Cartaz A4 editável e exportação. Abre o SVG na mesma pasta da imagem |
| [plano.json](plano.json) e [guiao_visual.pdf](saidas/guiao_visual.pdf) | Coordenadas, intertítulos e três fotogramas da curta exportada |
| [curta.mp4](saidas/curta.mp4) | Curta muda em H.264, 1280 × 720, 24 fps e 15 s |
| [resultado.json](saidas/resultado.json) | Medição, ambiente de montagem e SHA-256 das entradas e saídas |

## Montagem sem código

1. Abre a ilustração num editor. Cria um cartaz vertical e coloca título e autoria em caixas de texto que possas editar.
2. Cria um vídeo horizontal. Insere três cópias da imagem, cada uma com cinco segundos. Na primeira enquadra o balcão, na segunda o tambor e na terceira o cesto. Se usares zoom, confirma que a faixa clara continua dentro do plano.
3. Acrescenta os três intertítulos do guião visual. Exporta e revê os cortes e o fim do vídeo. Para comparar duas montagens, muda a ordem dos planos e pergunta a uma pessoa quando percebeu onde estava a meia.

## Reprodução da exportação

Usa Python 3.10+ com Pillow e ReportLab, Inkscape, FFmpeg com `drawtext` e `libx264`, `ffprobe` e DejaVu Sans, DejaVu Sans Bold e DejaVu Serif Bold. O SVG usa as famílias DejaVu instaladas no sistema. A opção `--fontes` permite indicar outra pasta com os três ficheiros TTF para a montagem.

```sh
python3 exemplos/atelier/montar.py --destino build/atelier
ffprobe -v error -count_frames -show_streams -show_format build/atelier/curta.mp4
```

Escolhe uma pasta de destino nova. A montagem reutiliza a imagem fornecida e corre localmente. O manifesto identifica os ficheiros de uma execução. Metadados e codificação podem variar entre ambientes.

## Origem da imagem

Ilustração gerada em 5 de novembro de 2026 para este projeto. Pedido original abaixo. A ferramenta devolveu a imagem e não identificou a revisão interna do modelo. A cena, os intertítulos, a composição do cartaz e a montagem pertencem ao projeto. As condições gerais estão no [ficheiro de licença da obra](../../LICENSE) e a licença das fontes incorporadas em [LICENCA_TIPOGRAFIA.txt](LICENCA_TIPOGRAFIA.txt).

```text
Use case: illustration-story.
Asset type: original key illustration for an educational book and a silent fifteen-second short titled “A Meia Testemunha”.
Create one wide landscape cinematic illustration, a single continuous image, with a restrained editorial gouache and subtle grain finish. A small fictional laundromat at night, empty of people, cobalt-blue front-loading washing machines under a pool of warm amber light, deep navy shadows, muted cream surfaces. Give the frame three distinct readable subjects for later camera crops. On the left foreground, one red ankle sock lies clearly on a light counter. In the middle, show a large circular washer door, with its glass and drum visible. On the right, a cream wicker laundry basket with a second matching red ankle sock caught over the OUTSIDE edge, clearly visible and draping down the exterior. Both socks are ordinary knitted red ankle socks with one narrow cream band around the cuff. Place the objects comfortably inside the image so they can be cropped independently. The second sock should be discoverable in the wide frame, without being hidden by shadow. The mystery comes from composition, ordinary objects and warm lighting. No other garments, people, faces, real brands, typography, numbers, signatures or watermarks.
```

## Evidência da execução

O cartaz e o guião exportados têm uma página A4 cada. O vídeo foi montado por recorte, zoom e texto a partir da mesma ilustração. O `ffprobe` contou 360 fotogramas numa faixa de vídeo, a 24 fps, e confirmou 15,000 s. O guião inclui imagens extraídas a 2,5 s, 7,5 s e 12,5 s. A primeira inspeção do guião revelou espaçamento irregular com fontes PDF de substituição. A versão entregue incorpora DejaVu e foi renderizada de novo.

A revisão visual conferiu as duas faixas claras no cartaz, a revelação no terceiro plano e o texto nos cortes. A experiência com espectadores fica proposta como extensão.
