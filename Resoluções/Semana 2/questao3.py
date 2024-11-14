# Pergunto o nome do Funcionário e deixo a primeira letra do nome maiúscula:
nome = str(input("Qual o nome do funcionário?\n")).capitalize()

# Pergunto a quantidade de horas trabalhadas semanalmente pelo funcionário e a quantidade de dependentes
hSemanais = int(input(f"Quantas horas por semana {nome} trabalha?\n"))
dependentes = int(input(f"Quantos dependentes {nome} tem?\n"))

# Multiplico as horas semanais por 4 para ter as horas trabalhadas mensalmente, 
# depois, multiplico por R$25.00 que é o quanto a empresa paga por hora:
salario_mes = (hSemanais * 4) * 25.00

# Somo o salário mensal com base nas horas com o numero de dependentes multiplicado por R$500.00,
# que é o valor que a empresa paga por dependente:
salario_total = salario_mes + (dependentes * 500)

# Mostro no terminal o Total do salário mensal do Funcionário:
print(f"{nome} terá um salario mensal de R${salario_total:.2f}")