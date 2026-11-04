# Progresso da terceira edição

Atualização: 04-11-2026. Branch `terceira-edicao-ia-referencia-2026`. [PR #2 em Draft](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/pull/2).

**Estado global: manuscrito ampliado e tecnicamente validado, ainda em desenvolvimento.** Foram integrados 50 capítulos em dez partes, incluindo 21 novos, três apêndices, 73 Prompt Labs, 73 referências e 58 entradas de glossário. O PDF tem 268 páginas físicas, incluindo capa e preliminares. Não se declara a obra concluída, pronta para publicação ou aprovada para merge.

## Checkpoint A — diagnóstico e arquitetura

### Retoma em curso: progressão e narrativa

O autor autorizou continuar em 04-11-2026, com progressão do básico à especialização, rigor factual, humor e leitura envolvente. Base confirmada `e990b891`; `main` continua em `975ade8`. A orientação está em `V3_LINHA_NARRATIVA.md`.

Já escritos: abertura investigativa original, história com fontes adicionais, camadas de explicação nos fundamentos e transições coerentes com a ordem real. O primeiro capítulo já não promete a primeira conversa num capítulo que afinal trata de história. Os aprofundamentos matemáticos são identificados como opcionais na primeira passagem.

Já executados: XOR construído, retorno e atualização Q, taxas condicionais, produtividade e energia sintéticas. **65 testes passaram** no conjunto completo. O commit remoto `7bf38ddb` guarda o código e os testes. A primeira compilação desta retoma passou com 277 páginas; ainda não é a composição final do ciclo. A bibliografia contém 14 entradas novas consultadas, a integrar nos casos setoriais.

Em curso: aprofundamento dos cinco capítulos da Parte VIII. Por fazer neste ciclo: fechar texto, compilar novamente, inspecionar PDF, atualizar contagens e confirmar CI do HEAD final. Os números de 268 páginas e 52 testes noutras secções deste registo descrevem o checkpoint anterior.

- Concluído: estado real do GitHub, PR #1 integrado, inexistência inicial da branch V3, criação da branch a partir de `975ade8`.
- Concluído: cópia local com a mesma árvore Git da base; leitura integral dos 29 capítulos e três apêndices; inspeção de bibliografia, validação estática, workflow e demonstração.
- Concluído: 30 testes existentes executados; 29 capítulos, 47 laboratórios e 41 referências verificados; integridade dos 52 registos reais de 03-11-2026 reavaliada, sem nova inferência.
- Concluído: matriz de cobertura e arquitetura em dez partes; três títulos com recomendação provisória.
- Este checkpoint inicial está preservado como diagnóstico. A produção posterior está registada abaixo; o antigo próximo passo já foi executado.

## Checkpoint B — arquitetura integrada

Concluídos o mapa de migração, a sequência em dez partes e a integração em `src/livro.tex`. Os nomes dos ficheiros conservam os identificadores históricos; não correspondem à numeração impressa. `V3_ESTRUTURA.json` verifica a ordem exata dos 50 capítulos e dos três apêndices. O percurso de leitura permite chegar às primeiras aplicações sem exigir a leitura prévia da matemática.

## Checkpoint C — produção e revisão

| Área | Produzido e integrado | Profundidade ainda por completar |
|---|---|---|
| I. Revolução | História, definições operacionais, ANI/AGI/ASI e limites de demonstrações; ficheiros 01 e 30 | Ampliar os ciclos históricos com casos documentados e revisão especializada |
| II. Máquina | ML, generalização, RL, arquiteturas generativas; cálculos de regressão, atenção e memória; revisão de 06–09 | Exercícios mais desenvolvidos de redes, otimização, avaliação fora da distribuição e multimodalidade |
| III. Conversar | Revisão dos fundamentos de prompts e raciocínio; contexto, memória e compressão; geração estruturada | Ensaios de seleção/compressão de contexto com modelos e diferentes tarefas |
| IV. Criar | Aplicações existentes revistas; novos projetos de imagem, audiovisual, música, voz, jogos e atividades sem código | Executar os projetos multimédia, guardar resultados autorizados e validar instruções com leitores não técnicos |
| V. Construir | Skills, pacote demonstrativo, supervisor, paralelismo, contratos, falhas e A2A; segurança e limites | Validar ativação numa aplicação de agentes e implementar uma integração MCP/A2A real, se mantida no âmbito dos laboratórios |
| VI. Adaptar | Fine-tuning, LoRA, QLoRA, distilação, quantização e estimativa de memória | Um treino real documentado e medições comparáveis de execução local; não realizados nesta sessão |
| VII. Operar | Núcleo de avaliação, autorização, segurança, observabilidade e governação preservado e complementado | Ensaio integrado de incidente e recuperação de equipa com modelo real |
| VIII. Sociedade | Cinco capítulos com estudos, métodos, populações, resultados e limites; trabalho, ciência, poder, relações e energia | Aprofundar educação, biotecnologia, agricultura, indústria, justiça e serviços públicos com casos próprios e mais fontes primárias |
| IX. Futuro | Modelos do mundo, robótica, consciência e cenários com evidência contrária; revisão do percurso profissional | Revisão científica independente e maior desenvolvimento dos paradigmas alternativos e consequências económicas |
| X. Laboratório | Seis projetos integrados, comparação offline executada e protocolo humano/IA separado das medições | Piloto com LLM bloqueado; estudo com participantes e restantes projetos não executados |

Foram corrigidas generalizações sobre recência de contexto, few-shot, unimodalidade, RLHF, alinhamento, criatividade e aprendizagem. A revisão distingue estilos de raciocínio de acesso a processos internos e separa resultados de estudos de recomendações. O glossário foi ampliado, ordenado e harmonizado. Fontes e alcance da consulta constam de `V3_FONTES_E_EVIDENCIAS.md`.

## Checkpoint D — exemplos executados e limites

- Executados: fundamentos matemáticos e estimativas; validador de pacote de skill e fichas; controlador com orçamento, dois especialistas paralelos e síntese; testes de falhas parciais e contratos. Os novos módulos acrescentam 22 testes aos 30 existentes: **52 passaram**.
- Executados: 12 regressões da Lavandaria; revalidação da integridade dos 52 registos reais históricos; ensaio determinístico novo em quatro casos e três modos. No ensaio novo, cada modo acerta dois de quatro; fluxo e único gastam quatro chamadas de componentes, equipa gasta doze, **zero chamadas LLM**. Isto não é um benchmark de inteligência ou uma comparação humana.
- Implementado, mas bloqueado antes da primeira inferência: piloto local novo com 32 chamadas de modelo planeadas. O runtime recusou a cópia incompleta do modelo; a tentativa de obter outra cópia falhou por ligação indisponível. Tamanho, hashes, erro e protocolo estão em `experiencias/equipas/README.md`. Nenhum resultado foi preenchido por simulação.
- Propostos, sem alegação de execução: treino LoRA/QLoRA, estudo com pessoas, produção multimédia e instalação/ativação real da skill. Os exemplos offline não precisam de API paga.

## Checkpoints E e F — integração e entrega de trabalho

Compilação LaTeX/BibTeX, validação estrutural, citações, referências cruzadas e verificações do log passaram. Inspeção das 268 páginas em quatro folhas de contacto, revisão ampliada de 20 páginas e verificação geométrica de todos os blocos de texto não identificaram cortes ou extravasamentos. Não substituem revisão científica ou leitura editorial integral da edição composta.

O GitHub Actions passou no push e no PR para a revisão de conteúdo `29364b6558ce40426f5e682058ad97f698bc40b7`: [execução do PR](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922570704), [execução do push](https://github.com/MPrazeres-1983/engenharia-de-prompts-codigo-oculto/actions/runs/41922563663). A atualização final de documentação volta a acionar a CI; o estado do HEAD está no PR.

O PR continua Draft porque a cobertura inicial de todas as áreas não demonstra profundidade final. `main@975ade8`, a licença, a capa e os resultados históricos foram preservados. Não foi feito merge, tag, release ou publicação.

## Commits persistentes de produção

SHAs abaixo são do GitHub, não da cópia local usada para preparar as alterações.

| Commit | Conteúdo |
|---|---|
| `b737f239` | Auditoria dos 29 capítulos, matriz, plano e checkpoint inicial |
| `be8e1f50` | Fundamentos e criação; cálculos e testes |
| `8175b32e` | Pacote de skill e controlador de equipa com testes |
| `cc9baa4a` | Capítulos de skills, multiagentes e interoperabilidade |
| `a23420da` | Adaptação e execução local |
| `1c2bf631` | Sociedade, evidência de impacto e cenários |
| `deed918a` | Integração em dez partes, revisão de capítulos, 73 labs e CI |
| `29364b65` | Correções tipográficas após composição |

O checkpoint final de documentação sucede a estes commits; o SHA pode ser obtido no HEAD da branch e na folha de rosto do PDF correspondente.

## Próximo passo exato

1. Verificar o HEAD e este checkpoint; continuar nesta branch e neste PR. Não reproduzir a auditoria nem reescrever os 21 capítulos como se não existissem.
2. Obter uma cópia íntegra do modelo indicado, confirmar o SHA-256 e a revisão do runtime, iniciar o servidor local e executar o piloto descrito em `experiencias/equipas/README.md` numa pasta nova. Se continuar bloqueado, conservar esse estado; não substituir inferências por stubs.
3. Registar pedidos, respostas, tokens disponíveis, tempos e falhas; validar o manifesto. Só então atualizar o capítulo de comparação com resultados efetivamente observados e limites da pequena amostra.
4. Aprofundar prioritariamente os cinco capítulos da Parte VIII: cada setor precisa de problema, mecanismo, estudo primário, efeitos demonstrados, limitações e caso de decisão. Expandir depois os exercícios de fundamentos, adaptação e criação de acordo com a tabela anterior.
5. Executar os projetos criativos e o treino que forem mantidos como demonstrações da edição final; para a comparação humana, definir protocolo, consentimento, participantes e avaliação antes de recolher dados. Não bloquear a investigação editorial independente destes ensaios.
6. Reavaliar a matriz, a progressão e os critérios de aceitação do pedido. Só quando a profundidade e a evidência forem adequadas se poderá retirar o estado de desenvolvimento; manter o PR Draft até essa decisão explícita.

## Regras para retoma

Ler este ficheiro, `V3_VALIDACAO.md` e o histórico da branch no GitHub. Confrontar o HEAD remoto com o último checkpoint. Não recriar branch nem repetir a segunda edição. Não fazer merge. Não confundir itens previstos com capítulos produzidos.

## Decisões reservadas ao autor

Título comercial definitivo; revisão independente; suficiência da profundidade e da extensão; capa final; publicação e merge. Nenhuma dessas decisões é implicitamente aprovada por um build verde.
