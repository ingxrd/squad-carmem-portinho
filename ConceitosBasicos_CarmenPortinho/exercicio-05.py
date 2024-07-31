#Escreva um programa que calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de
    # avião 600km/h
    # carro 100km/h
    # onibus 80km/h

distancia = int(input("Insira a distância em KM para saber o tempo de viagem: "))
aviao = distancia/600
carro = distancia/100
onibus = distancia/80

print(f'O tempo de viagem para {distancia} KM é:')
print(f'Avião: {aviao:.2f} horas')
print(f'Carro: {carro:.2f} horas')
print(f'Ônibus: {onibus:.2f} horas')