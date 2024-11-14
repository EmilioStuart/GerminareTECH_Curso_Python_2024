quantidade = int(input("Insira a quantidade de produtos que deseja comprar: "))

if (2 <= quantidade <= 4):
    desconto = 0.5
elif (5 <= quantidade <= 7):
    desconto = 0.10
elif (quantidade >= 8 ):
    desconto = 0.15

precoTotal = 0

for i in range(quantidade):
    preco = float(input(f"Insira o preco do {i}° produto: "))
    precoTotal += preco--------
