# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    # Verifica se o prompt contém palavras-chave relevantes
    palavras_chave = ["inteligência artificial", "sistemas de recomendação online", "exemplos de conversação", "explique conceitos", "dicas de tecnologia"]
    
    # Convertendo o prompt para minúsculas para facilitar a comparação
    prompt_lower = prompt.lower()
    
    # Verifica se o prompt contém pelo menos uma das palavras-chave
    for palavra_chave in palavras_chave:
        if palavra_chave in prompt_lower:
            return "O prompt está adequado."
    
    # Se nenhuma palavra-chave for encontrada, sugere ao usuário incluir palavras-chave relevantes
    return "O prompt não está adequado. Inclua palavras-chave relevantes."

# Entrada do usuário
prompt_usuario = input()

# Avaliar o prompt do usuário e obter o feedback
feedback_usuario = avaliar_prompt(prompt_usuario)

# Exibir feedback
print(feedback_usuario)
