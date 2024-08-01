"""
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))

imc = peso /(altura * altura)

print(f'Seu Imc é {imc:.2f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc <= 24.9:
    print('Você está com o peso normal.')
elif 25.0 <= imc <= 29.9:
    print('Você está com sobrepeso.')
elif 30.0 <= imc <= 34.9:
    print('Você está com obesidade grau 1.')
elif 35.0 <= imc <= 39.9:
    print('Você está com obesidade grau 2.')
else:
    print('Você está com obesidade grau 3 (obesidade mórbida).')