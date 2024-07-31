'''
Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; 
caso contrário, é reprovado.
'''

notaAluno = float(input("Insira sua pontuação na prova: "))
if notaAluno >= 7:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado")
