# -*- coding: utf-8 -*-

def encontrar_resposta(pergunta, arquivo_respostas, nome_chatbot):
  """Encontra a resposta para uma pergunta em um arquivo de respostas,
  substituindo a palavra "CHAT" pelo nome do chatbot.

  Args:
    pergunta: A pergunta do usuário.
    arquivo_respostas: O caminho do arquivo de respostas.
    nome_chatbot: O nome escolhido pelo usuário para o chatbot.

  Returns:
    A resposta correspondente, com o nome do chatbot substituído.
  """

  pergunta = pergunta.lower()  # Converte a pergunta para minúsculas
  with open(arquivo_respostas, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
      pergunta_arquivo, resposta_arquivo = linha.strip().split('=')
      if pergunta_arquivo.lower() == pergunta:
        return resposta_arquivo.replace("CHAT", nome_chatbot)

  return "Desculpe, não encontrei uma resposta para essa pergunta."


# Solicita o nome do  usuário
meu_nome = input("Como você quer ser chamado? ")

# Solicita o nome do chatbot ao usuário
nome_chatbot = input("Como você quer me chamar? ")

# Arquivo com as perguntas e respostas
arquivo_respostas = "respostas.txt"

# Loop principal
while True:
  pergunta = input ("{}:".format(meu_nome))
  #pergunta = input("{}:".format(nome_chatbot))

  resposta = encontrar_resposta(pergunta, arquivo_respostas, nome_chatbot)
  #print(resposta)
  print(f"{nome_chatbot}:{resposta}")