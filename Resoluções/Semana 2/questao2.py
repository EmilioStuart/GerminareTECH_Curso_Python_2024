# Pergunto ao usuário o tamanho do piso e o valor unitário de cada lata:
piso = float(input("Digite a área do piso a ser pintado em metros quadrados: "))
valor_lata = float(input("Digite o valor da lata em reais: "))

lata_pinta = 15 # Cada lata pinta 15m² de piso

# Vejo quantas latas serão necessárias para pintar o piso:
quant_latas = piso // lata_pinta

# Calculo qual o valor gasto para comprar as latas
preco_latas = valor_lata * quant_latas

# Mostro no Terminal o total de latas que serão necessárias e o valor que será gasto para comprá-las:
print(f"Você precisará de{quant_latas: .0f} latas de tinta para pintar seu piso")
print(f"Vão custar um total de R${preco_latas: .2f}")