'''
4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21
'''

def calcular_conversao(valor_reais):
    taxas_conversao = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suíço": 0.42,
        "Euro": 5.36,
        "Libra Esterlina": 6.21
    }
    
    for moeda, taxa in taxas_conversao.items():
        valor_moeda = valor_reais / taxa
        print(f"Com R$ {valor_reais:.2f}, você pode comprar {valor_moeda:.2f} {moeda}.")

valor_reais = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))

calcular_conversao(valor_reais)