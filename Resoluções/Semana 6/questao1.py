# Crio uma função onde por meio da manipulação de string, "percorro" a String de trás para frente:
def inverter_string(texto):
    # Retorna a string invertida:
    return texto[::-1]

# Peço ao usuário a string
string = str(input("Insira a String: "))

# Realizo a chamada da função "inverter_string()"
stringInvertida = inverter_string(string)

# Utilizando a função "len()" conto a quantidade de dígitos na String
digitosString = len(string)

# Mostro ao usuário a String invertida e a quantidade de dígitos da String
print(f"\n'{string}' ao contrário é {stringInvertida}")
print(f"E contém {digitosString} dígitos")