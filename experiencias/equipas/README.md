# Piloto V3: fluxo fixo, chamada única e equipa

**Estado em 04-11-2026: ensaio com LLM bloqueado antes da inferência.** O controlador e os seus testes com adaptadores determinísticos foram executados. Não existem resultados novos de desempenho de um LLM nesta pasta.

## O que aconteceu

A cópia local de `qwen2.5-0.5b-instruct-q4_k_m.gguf` tinha 255381504 bytes. O runtime recusou carregá-la com `tensor 'blk.1.ffn_down.weight' data is not within the file bounds, model is corrupted or incomplete`. Hash encontrado: `7e5fb2f526ad52876a3417b1f61931ee6405aab6deea974777c84b8f5311b62d`; hash de referência do ensaio anterior: `74a4da8c9fdbcd15bd1f6d01d621410d31c6fc00986f5eb687824e7b93d7a9db`.

A tentativa de ligação à revisão oficial do modelo terminou com `Proxy CONNECT aborted due to timeout`. Não foi pedido acesso elevado nem substituído o modelo por um ficheiro sem proveniência. O arquivo do runtime conservou o hash de referência `31cc3a6bc638ac6c48dc4b1b74888f1eaadf3d14227c1e5f67daf9a49541d97a`.

Isto não altera os registos históricos de 03-11-2026, que continuam na pasta `llm_local`, com respostas e hashes verificáveis. Não prova que o ficheiro estava incompleto quando essas execuções foram feitas. Prova que a cópia disponível nesta sessão não permitia iniciar o novo ensaio.

Na retoma editorial do mesmo dia, a ligação à revisão fixada foi novamente tentada e terminou com `curl: (28) Operation timed out after 5010 milliseconds with 0 bytes received`. O estado continua bloqueado, sem inferências novas. O treino de adaptação linear 2×2 em `experiencias/adaptacao_linear` é outra experiência, executada sem esse modelo; não completa este piloto.

## Desenho fechado antes da tentativa

Quatro pedidos sintéticos, duas seeds (42 e 1337), três modos. O fluxo usa regras, sem LLM. A chamada única usa um LLM. A equipa usa duas chamadas de especialistas em paralelo, com o mesmo snapshot, e uma síntese. No total estão planeadas 32 chamadas reais de modelo, com contexto novo, temperatura 0.2 e máximo de 96 tokens por chamada.

O objetivo é acertar **categoria e fonte**. Não se gera resposta ao cliente nem se consulta o estado real de uma reclamação. O modo de estado devolve fonte nula porque estes documentos não contêm esse registo. O custo não é igual entre modos: apresentar contagens, tokens, erros e tempo juntamente com o acerto. Segundos incluem fila do servidor e não medem isoladamente o ganho de paralelismo.

Não há participantes humanos nem teste reservado representativo de produção. As seeds repetem os mesmos casos. Não contar oito execuções como oito casos independentes. Não afinar os prompts com base nos resultados sem criar outra versão e outro ensaio.

## Executar quando houver um modelo íntegro

1. Obter o [modelo oficial na revisão fixada](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/tree/9217f5db79a29953eb74d5343926648285ec7e67), confirmar licença e SHA-256. Não redistribuir os pesos neste repositório.
2. Usar llama.cpp b11960, conforme a documentação já fixada na segunda edição; guardar logs de arranque e confirmar modelo e configuração.
3. Iniciar apenas em loopback, por exemplo:

```bash
llama-server --model qwen2.5-0.5b-instruct-q4_k_m.gguf \
  --host 127.0.0.1 --port 8766 --ctx-size 8192 --parallel 2 \
  --threads 4 --n-gpu-layers 0 --no-webui
```

4. Na raiz do projeto, escolher uma pasta nova:

```bash
python3 experiencias/equipas/executar.py \
  --modelo-ficheiro /caminho/qwen2.5-0.5b-instruct-q4_k_m.gguf \
  --output experiencias/equipas/resultados/execucao-nova
```

O script recusa pasta já utilizada e hash diferente. Guarda casos, fontes do executor, configuração declarada, pedidos, respostas brutas e resumo. Confirmar a configuração real nos logs continua a ser responsabilidade do operador. Outro modelo exige alterar explicitamente a identificação e o hash esperado e constitui outro ensaio.

## Sem modelo ou sem rede

```bash
python3 -m exemplos.laboratorio.equipas
python3 -m unittest discover -s tests -p test_equipas.py -v
```

Este percurso verifica contratos, concorrência de orçamento, falha parcial e encaminhamento. Não mede inteligência nem superioridade de equipas. Os limites estão também no capítulo de multiagentes e no relatório V3.
