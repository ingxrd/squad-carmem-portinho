'''
 Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas
'''

ladoA = float(input("Insira o Lado A do triangulo: "))
ladoB = float(input("Insira o Lado B do triangulo: "))
ladoC = float(input("Insira o Lado C do triangulo: "))

if ladoA == ladoB and ladoB == ladoC:
    print("Esse é um triângulo equilátero")
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print("Esse é um triângulo isósceles")
else:
    print("Esse é um triângulo escaleno")