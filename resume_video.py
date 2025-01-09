import openai

def resumir_texto(texto):
    prompt = f'''Voce atuara em uma plataforma de ensino a distancia.
    Assuma a função de um ferramenta que resume videos transcritos.
    Resuma tudo trazendo os principais pontos em topicos.
    Faça o resumo da forma mais detalhada possivel e perdendo a menor quantidade de informação possivel.
    O texto do video transcrito é: \n{texto}'''

   #openai.api_key = '#chave API aqui'
    try:
        resposta = openai.chat.completions.create(
            model="gpt-4o-mini",  # ou "gpt-4"
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000 # Defina o número máximo de tokens
        )
        print('---------------Transcrição resumida---------------')
        return resposta.choices[0].message.content  # Retorna o resumo
    except Exception as e:
        print(f"Erro ao chamar a API do GPT: {e}")
        return texto  # Retorna o texto original em caso de erro