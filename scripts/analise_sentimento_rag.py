"""Baseline heurística de intenção: não executa RAG, sentimento ou um LLM.

O nome histórico do ficheiro mantém compatibilidade com a primeira edição.
Não há confiança calibrada; uma palavra-chave pode ser insuficiente ou ambígua.
O exemplo integrado está em exemplos/lavandaria.
"""

def classificar_feedback(texto):
    if not isinstance(texto, str):
        raise TypeError("texto deve ser uma string")
    if "erro" in texto.lower() or "crash" in texto.lower():
        categoria, humano = "Bug Report", True
    elif "como" in texto.lower() or "?" in texto.lower():
        categoria, humano = "Dúvida Técnica", True
    elif "gostei" in texto.lower():
        categoria, humano = "Elogio", False
    else:
        categoria, humano = "Indeterminado", True
    return {"intent": categoria, "needs_human": humano,
            "metodo": "heuristica_palavras_chave_sem_LLM"}

if __name__ == "__main__":
    casos = [
        "O sistema dá erro 500 ao abrir o PDF.",
        "Como posso mudar a temperatura do modelo no prompt?",
        "Gostei muito do design."
    ]
    
    for caso in casos:
        resultado = classificar_feedback(caso)
        print(f"Resultado: {resultado}")
