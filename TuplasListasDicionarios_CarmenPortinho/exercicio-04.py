'''
4. Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
'''

contatos = {
    "Alice": "1234-5678",
    "Bob": "8765-4321",
    "Carlos": "5678-1234"
}

nome_procurado = input("Digite o nome do contato que deseja procurar: ")

if nome_procurado in contatos:
    print(f"O telefone de {nome_procurado} é {contatos[nome_procurado]}.")
else:
    print(f"Contato {nome_procurado} não encontrado.")
    