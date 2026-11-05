# Um adaptador aprendido que cabe numa conta

Experiência executada em 04-11-2026, com dados inteiramente sintéticos, Python e biblioteca padrão. A base é a matriz identidade 2×2 e permanece congelada. Treinam-se os dois fatores de uma atualização de posto um, com escala alfa/r igual a um. **Não é fine-tuning de um LLM, QLoRA ou avaliação de recursos de GPU.**

```bash
python3 -m exemplos.laboratorio.adaptacao
python3 -m unittest discover -s tests -p test_adaptacao.py -v
```

O ficheiro de resultado conserva a configuração, treino, teste, pesos obtidos, perdas e hash do código executado. Não foi escolhida a melhor seed; a inicialização está definida no código e não há amostragem aleatória. Diferenças mínimas de arredondamento entre ambientes não são novas descobertas.

## Primeiro problema: atualização representável

Com base identidade, o alvo é `[[2,2],[-1,-1]]`. A diferença para a base é `[[1,2],[-1,-2]]`, de posto um. Treinam-se as entradas `(±1,0)` e `(0,±1)`; os três casos reservados são combinações diferentes dessas coordenadas. A perda desce de 2,5 para menos de 1e-12 e o erro reservado também fica abaixo desse limite nesta configuração. Esta tarefa linear construída é exatamente representável; não mede generalização em linguagem ou num domínio real.

## Segundo problema: capacidade insuficiente

Mantemos base, entradas e processo, mas o alvo passa a ser duas vezes a identidade. A atualização necessária é a identidade, de posto dois. Um produto de fatores de posto um não a representa. Com a perda definida no script, o mínimo teórico neste conjunto é 0,25; o treino observado chega a 0,25, partindo de 0,5. O capítulo demonstra o limite para este problema, em vez de concluir que «mais passos» resolveriam a restrição.

## O que foi verificado

Cinco testes verificam a preservação da base, gradientes por diferenças finitas, previsão nos casos reservados, limite de posto e rejeição de dados/configurações inválidas. Na escala 2×2, os quatro parâmetros dos fatores não poupam parâmetros face aos quatro da matriz base. A escolha torna o mecanismo visível; a contagem em matrizes maiores é outro cálculo.

Não foram medidos tempo de hardware, energia, memória de treino ou desempenho de um modelo de linguagem. Os testes avaliam esta implementação matemática. O workflow volta a executar o exemplo e guarda a saída no artefacto de validação.
