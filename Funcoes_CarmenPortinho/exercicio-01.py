# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#iniciando uma lista global vazia
soma_numeros = []

#função para add os numeros e retorna a soma
def soma(resposta):    
    
    soma_numeros.append(resposta)

    return sum(soma_numeros)


#capturando os 3 numeros e enviando para a funcao
for index in range(3):
    soma_total = soma(resposta = int(input(f'Digite o  {index + 1}º número: ')))
    
#exibindo o resultado
print('\nA soma dos números é:', soma_total)