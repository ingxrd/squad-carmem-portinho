# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

#iniciando uma lista vazia
soma_resposta = []

def soma(resposta): #função que pega a resposta do input e joga para a lista
    return soma_resposta.append(resposta)


print('~ Somatorio de numeros ~ ')
for index in range(5): #faz o loop de até 3 numeros, mas é livre para colocar quantos quiser
    soma(resposta = int(input(f'Digite o {index+1}º: '))) #chama a função soma() e já tem a entrada do usuario e já adiciona na lista lá na função


#mostra a lista com os 3 numeros já somando os numeros.
print(f'A soma dos numeros é:', sum(soma_resposta))