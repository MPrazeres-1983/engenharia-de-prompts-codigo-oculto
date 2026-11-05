# Incidente dos cinco dias

Ensaio sintético da Lavandaria, executado em 5 de novembro de 2026. A política fictícia em `politicas.json` muda de dez para cinco dias úteis. As duas versões têm o mesmo identificador de documento.

## Repetir

A partir da raiz, com Python 3.10+ e biblioteca padrão:

```sh
python3 -m exemplos.laboratorio.operacao
python3 -m unittest discover -s tests -p 'test_operacao.py' -v
```

## O que aconteceu

| Etapa | Entrada na cache | Política vigente | Saída para o utilizador |
|---|---|---|---|
| Base | v1, 10 dias | v1, 10 dias | Prazo de 10 dias úteis |
| Falha injetada | v1, 10 dias | v2, 5 dias | Encaminhamento sem prazo |
| Recuperação | v1, 10 dias e v2, 5 dias | v2, 5 dias | Prazo de 5 dias úteis |

A cache legada usa só o identificador de documento. A sonda recebe uma proposta antiga com formato válido. A decisão compara a versão e o SHA-256 da política vigente, obtida independentemente da cache. O hash é calculado sobre o objeto da política serializado em JSON compacto com chaves ordenadas. A verificação separada do prazo deteta uma proposta com identificadores atuais e valor errado. O encaminhamento é representado por um estado no registo. A recuperação mantém v2 vigente e passa a consultar a cache pela chave `(documento, versao)`.

[Resultado efetivo da execução](resultado.json). A proposta antiga aparece no registo de teste para diagnóstico. A resposta contida inclui só estado e motivo. Os seis testes conferem a reprovação da entrada antiga, a recuperação, a integridade da versão, o prazo, a estrutura e a reprodução do registo.

O ensaio usa um processo local, duas políticas e uma cache em memória. São zero chamadas a LLM e zero operações num serviço externo. Em produção, o fluxo teria de ligar o estado a uma fila e verificar autorização, vigência e efeitos da mudança com dados adequados ao serviço.
