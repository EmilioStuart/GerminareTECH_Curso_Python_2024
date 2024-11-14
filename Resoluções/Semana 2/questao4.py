# Peço ao usuário a população inicial, a taxa de crescimento anual e o período em anos da simulação:
populacaoInicial = int(input("Insira a população inicial: "))
taxaCrescimento = float(input("Insira a taxa crescimento anual (em decimal): "))
periodo = int(input("Insira o período de anos a serem simulados: "))

# Aplico uma fórmula para calcular o crescimento populacional sem o uso da estrutura de repetição:
populacaoFinal = populacaoInicial * (1 + taxaCrescimento) ** periodo

# Mostro no terminal o crescimento da população ao final do período:
print(f"Após {periodo} anos a população ficou em {populacaoFinal:.0f} habitantes")
