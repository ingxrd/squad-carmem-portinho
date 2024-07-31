'''Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro'''


login = 'admin'
senha = 'admin123'

while True:
    acesso_login = input('Digite o login: ')
    acesso_senha = input('Digite a senha: ')
    
    if login == acesso_login and senha == acesso_senha:
        print('Acesso permitido !')
        break
    else:    
        print('Mensagem de Erro !')