# Da biblioteca random importo apenas a função randint, que gera numeros aleatórios
from random import randint

# Instancio a variável saldo em 100 pontos
saldo = 100

while (saldo > 0):
    # Mostro ao usuário o saldo que ele possui:
    print("Seu saldo atual é de ", saldo)

    # Peço ao usuário o valor que ele deseja apostar:
    aposta = float(input("Quanto você deseja apostar?\n"))

    # Verifico se o usuário possui saldo o sulficiente para apostar:
    if (aposta > saldo):
        print("Você não possui saldo o sulficiente.")
        continue

    # Retiro o valor da aposta do saldo
    saldo -= aposta

    # Instancio o dado 1 com um valor aleatório de 1 à 6 e mostro ao usuário:
    dado1 = randint(1,6)
    print("Dado 1: ", dado1)

    # Instancio o dado 2 com um valor aleatório de 1 à 6 e mostro ao usuário:
    dado2 = randint(1, 6)
    print("Dado 2: ", dado2)

    # Somo o valor dos dados e mostro ao usuário:
    soma = dado1 + dado2
    print("A soma dos dados é ", soma)

    # Se a soma dos dados for 7 ou 11, o usuário recebe o dobro do valor apostado
    if((soma == 7) or (soma == 11)):
        print(f"Parabéns! Você ganhou {aposta * 2} ponto.")
        saldo += (aposta * 2)
    # Se for diferente de 7 ou 11, o usuário como penalidade perderá 20 pontos
    else:
        print(f"Infelizmente você perdeu 20 pontos. Tente Novamente")
        saldo -= 20

print("Seu saldo acabou. Obrigado por jogar!")