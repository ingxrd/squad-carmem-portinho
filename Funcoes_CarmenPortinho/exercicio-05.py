'''
Crie uma função chamada contar_vogais que recebe uma string
como parâmetro. Implemente a lógica para contar o número de vogais
na string e retorne o total de vogais. Solicite ao usuário para inserir uma
frase e utilize a função para contar as vogais.
'''

def contar_vogais(string):
    string = string.lower()
    contagem = {} #usando dicionario pq listas nao suportam indexação de strings
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            contagem[i] = string.count(i)
    return contagem


frase = input("Digite uma frase: ")
contagem_vogais = contar_vogais(frase)

total_vogais = sum(contagem_vogais.values())

print(f"Contagem de cada vogal: {contagem_vogais}")
print(f"Total de vogais na frase: {total_vogais}")
