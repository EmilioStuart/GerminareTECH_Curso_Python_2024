# Peço ao usuário pelo tempo em segundos:
segundos_iniciais = int(input("Insira os segundos: "))

# Dividir os segundos por 3600 para descobrir o total de horas
horas = segundos_iniciais // 3600 

# O que restou das horas, divido por 60 para obter os minutos:
minutos = (segundos_iniciais % 3600) // 60 
segundos = (segundos_iniciais % 3600) % 60

# Mostro o resultado no terminal:
print(f"{horas}h {minutos}m {segundos}s")