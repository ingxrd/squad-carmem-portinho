''' 2 - Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

# Primeiro irei solicitar a pessoa usuário em que turno ela estuda:
turno = input("Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

#Depois defo as regras de tomada de decisão para imprimir a  mensagem de acordo com o turno:
if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")