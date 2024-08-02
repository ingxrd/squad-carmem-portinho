'''
Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra.
'''
#In the next block, a dictionary representing a shopping cart will be created.
shopping_cart = {
    'yogurt': 2,
    'cheese': 3,
    'juice': 6,
    'bread': 4   
} # type: ignore
#In the next block, the prices of the products will be showed
product_prices = {
    'yogurt': 5.00,
    'cheese': 33.00,
    'juice': 10.00,
    'bread': 5.99   
}
#In the next block, the function to calculate the total of the shopping cart will be showed:
def calculate_total(shopping_cart, p)