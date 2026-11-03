import json

"""Extração heurística ilustrativa; sem modelo, RAG ou confiança calibrada."""

def extrair_dados_prompt(texto_bruto):
    if not isinstance(texto_bruto, str):
        raise TypeError("texto_bruto deve ser uma string")
    texto = texto_bruto.casefold()
    if any(p in texto for p in ["erro", "crash", "falha"]):
        classe = "bug"
    elif any(p in texto for p in ["acesso", "login", "palavra-passe"]):
        classe = "login"
    else:
        classe = "desconhecido"
    resultado = {
        "metodo": "heuristica_palavras_chave_sem_LLM",
        "tipo_problema": classe,
        "urgencia": "desconhecida",
        "descricao_curta": texto_bruto[:120],
        "precisa_resposta_humana": True
    }
    return json.dumps(resultado, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    exemplo = "O meu acesso ao servidor crashou quando tentei fazer o push."
    print(extrair_dados_prompt(exemplo))
