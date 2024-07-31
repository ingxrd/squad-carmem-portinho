# Faça um Programa que peça dois números e imprima o maior deles

#faço a captura dos dados, podendo ser inserido um float também
numero1 = input('Digite o 1ª numero: ')
numero2 = input('Digite o 2ª numero: ')

#faço a comparação dos números qual é o maior
if numero1 > numero2:
    #caso o numero 1 seja o maior, ele vai para a variável que chamei de 'maior'
    maior = numero1
else:
    #caso não seja, cai no 'else' e então é o segundo numero o maior entre eles
    maior = numero2

#exibindo o numero maior
print(f'\nO maior número é {maior}')