# 1. Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime.
# As perguntas são:
# ""Telefonou para a vítima?""
# ""Esteve no local do crime?""
# ""Mora perto da vítima?""
# ""Devia para a vítima?""
# ""Já trabalhou com a vítima?""
# O programa deve no final emitir uma classificação sobre a participação
# da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
# ""Assassino"".
# Caso contrário,ele será classificado como""Inocente"".

#listas globais utilizadas no programa
lista_resposta = []
lista_resposta_final_sim = []


### Historinha feita com ajuda do nosso amigo CHATGPT

tittle = '~ Curta interativo: O Silêncio das Dívidas" ~'
print('\n' + tittle + '\n')
print('Em uma pequena cidade onde todos se conheciam, o assassinato de Clara Rodrigues chocou a comunidade. Clara era uma respeitada empresária local e sua morte trouxe medo e desconfiança. O detetive Jorge Carvalho foi chamado para investigar o caso.\n\nClara foi encontrada em seu escritório, uma cena que parecia limpa demais para um crime tão brutal.\n\nJorge sabia que o assassino conhecia bem a vítima. Jorge começou suas investigações interrogando os principais suspeitos. Suas perguntas eram diretas e objetivas, buscando eliminar os inocentes e focar nos culpados.')

#começando a interação com o usuário e montando a historia
resposta = str(input('\n\nPara começar... Digite o seu nome: '))
nome = resposta.capitalize()

#perguntas
print('\nTelefonou para a vítima? perguntou Jorge.')
resposta = str(input('Digite "SIM" OU "NÃO": ')).lower()
lista_resposta.append(resposta)

print('\nEsteve no local do crime?')
resposta = str(input('Digite "SIM" OU "NÃO": ')).lower()
lista_resposta.append(resposta)

print('\nMora perto da vítima?')
resposta = str(input('Digite "SIM" OU "NÃO": ')).lower()
lista_resposta.append(resposta)

print('\nDevia para a vítima?')
resposta = str(input('Digite "SIM" OU "NÃO": ')).lower()
lista_resposta.append(resposta)

print('\nJá trabalhou com a vítima?')
resposta = str(input('Digite "SIM" OU "NÃO": ')).lower()
lista_resposta.append(resposta)

for index, resposta_final in enumerate(lista_resposta):
    # print(resposta_final)
    if resposta_final == 'sim':
        lista_resposta_final_sim.append(resposta_final)


#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como ""Assassino"". Caso contrário,ele será classificado como""Inocente"".
if len(lista_resposta_final_sim) <= 2: 
    print(lista_resposta_final_sim)
    print(f'\n~ {nome} estava visivelmente abalado(a), mas suas respostas não deram pistas conclusivas. mas é Suspeito(a)! ~ ')

elif len(lista_resposta_final_sim) == 3 or len(lista_resposta_final_sim) == 4:
    print(lista_resposta_final_sim)
    print(f'\n~ {nome} estava nervoso(a), mas suas respostas eram consistentes com o que Jorge já sabia. Pois pode ser um(a) Cúmplice! ~ ')

elif len(lista_resposta_final_sim) == 5: 
    print(lista_resposta_final_sim)
    print(f'\nJorge analisou todas as respostas e percebeu um padrão: {nome}(~ Assassino(a)! ~ ) era o único que "Telefonou para a vítima","Esteve no local do crime", "Mora perto da vítima", "Devia para a vítima" e já tinha trabalhado com a vítima . \nCom essas informações, Jorge decidiu investigar mais a fundo o passado de {nome} e descobriu evidências de que ele(a) havia forjado documentos para tentar encobrir seu crime.')

    print(f'Com a pressão das provas, {nome} confessou o crime. Ele(a) havia matado Clara! \nO caso foi encerrado, mas a pequena cidade nunca mais foi a mesma depois da tragédia.')

else: 
    print(lista_resposta_final_sim)
    print(f'\n~ {nome} parecia tranquilo(a), e Jorge descartou a possibilidade de um ressentimento escondido. {nome} é Inocente! ~ ')

