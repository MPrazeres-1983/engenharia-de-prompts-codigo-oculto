# Ensaio local com inferência real — 3 de novembro de 2026

52 chamadas reais, 13 casos fictícios, duas variantes por tarefa e duas seeds (42 e 1337). Sem chaves, serviços pagos ou dados pessoais. Os casos, respostas esperadas e prompts estão em `executar.py`; foram fixados antes das chamadas. Não houve ajuste posterior aos resultados.

Modelo: [Qwen2.5-0.5B-Instruct-GGUF oficial](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/tree/9217f5db79a29953eb74d5343926648285ec7e67), quantização Q4_K_M, licença Apache-2.0. Runtime: [llama.cpp b11960](https://github.com/ggml-org/llama.cpp/releases/tag/b11960), commit `8642541b2`. CPU, quatro threads, contexto 8192, uma sequência de cada vez. Pesos e executáveis não são incluídos no repositório.

O [manifesto](resultados/2026-11-03/manifesto.json) identifica revisões, hashes SHA-256, hardware e parâmetros. Cada linha das [saídas brutas](resultados/2026-11-03/saidas.jsonl) conserva pedido, resposta completa do servidor, uso de tokens, seed, data UTC e latência. O [resumo](resultados/2026-11-03/resumo.json) regista contagens; a [revisão semântica](resultados/2026-11-03/revisao_semantica.json) explicita os critérios e juízos editoriais sobre as 12 respostas documentais.

## Resultados observados

| Tarefa | Variante | Critério | Resultado |
|---|---|---|---|
| Classificação, seis mensagens | Zero-shot | Etiqueta exata, sem remover texto adicional | 6/12 |
| Classificação, mesmas mensagens | Few-shot, quatro demonstrações distintas dos casos | Etiqueta exata | 11/12 |
| Três pedidos documentais | Só instrução de JSON | JSON válido / contrato e proveniência | 6/6 / 0/6 |
| Mesmos pedidos documentais | Mesmo prompt + esquema no runtime | JSON válido / contrato e proveniência | 6/6 / 1/6 |
| Quatro durações | Pedido direto + esquema | Inteiro exato ou `null` quando indeterminado | 1/8 |
| Mesmas durações | Instrução de decomposição + mesmo esquema | Mesmo critério | 0/8 |

Todas as 52 chamadas terminaram com `finish_reason=stop`, sem falhas HTTP, recusas ou truncamento pelo limite de geração. Latência mediana observada: 0,5901 s; intervalo 0,3678–7,1718 s. É tempo do cliente neste ambiente, não um benchmark de velocidade.

Os seis objetos da variante com esquema respeitam a estrutura concreta; cinco falharam a proveniência no validador da Lavandaria. O único que passou respondeu **“48 horas”**, citando corretamente uma política que **não estabelece prazo fixo**. O validador verifica campos e excertos, não implicação lógica. Este é um contraexemplo real à ideia de que um contrato e uma citação bastam para provar correção. Nenhuma das 12 respostas documentais cumpre todos os critérios funcionais predefinidos. A revisão foi feita pelo assistente durante a edição, sem painel humano independente.

Nas durações, saídas como `{"minutos":30}` para 10:00–13:00 são JSON válido e cálculo errado. A variante de decomposição não mostrou melhoria nesta amostra. Não se reproduziu few-shot CoT, ToT ou self-consistency, nem se observou o raciocínio interno do modelo.

## Reproduzir sem sobrescrever a evidência

Obtém o build e o ficheiro de pesos oficiais acima e verifica os hashes do manifesto. Com o executável disponível, inicia o servidor num terminal:

```bash
llama-server --model qwen2.5-0.5b-instruct-q4_k_m.gguf --host 127.0.0.1 --port 8765 --ctx-size 8192 --parallel 1 --threads 4 --n-gpu-layers 0 --no-webui
```

Na raiz do repositório, noutro terminal:

```bash
python3 experiencias/llm_local/executar.py --output /tmp/lavandaria-nova-execucao
```

O executor recusa uma pasta que já contenha `saidas.jsonl`. Usa Python 3.10+ e biblioteca padrão. `--base-url` e `--model` permitem outros servidores compatíveis; essa mudança constitui outro ensaio, cuja configuração deve ser registada. Termina o servidor após a experiência.

## Alcance

Um modelo de 0,5 mil milhões de parâmetros, quantizado e anterior à data editorial, não representa o estado dos modelos disponíveis em 2026. São casos sintéticos pequenos, com critérios definidos para demonstração; não são um teste reservado representativo de clientes. Repetir a seed sobre o mesmo caso não cria casos independentes. Não se conclui superioridade geral de uma técnica, fornecedor ou arquitetura. Os 47 laboratórios não foram todos executados com modelos.

A demonstração principal e a CI continuam offline e determinísticas. Estas experiências não acrescentam um servidor MCP, autenticação real ou autorização para operar um serviço de produção.
