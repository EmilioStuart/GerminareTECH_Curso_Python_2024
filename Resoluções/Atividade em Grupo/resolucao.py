# Importa o módulo random para gerar números aleatórios
from random import randint

# Alfabeto base usado para codificação e decodificação
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

# Função para criptografar uma letra com base na chave
def criptografarLetra(letra, chave):
    if letra == ' ':
        return ' '  # Preserva o espaço
    pos = alfabeto.find(letra)  # Encontra a posição da letra no alfabeto
    nova_pos = (pos + chave) % 26  # Aplica o deslocamento com a chave (circular)
    return alfabeto[nova_pos]  # Retorna a letra criptografada

# Função para decodificar uma letra com base na chave
def decodificarLetra(letra, chave):
    if letra == ' ':
        return ' '  # Preserva o espaço
    pos = alfabeto.find(letra)  # Encontra a posição da letra original
    nova_pos = (pos - chave) % 26  # Inverte o deslocamento (circular)
    return alfabeto[nova_pos]  # Retorna a letra decodificada

# Criptografa uma mensagem inteira usando uma chave fixa
def criptografarChave(mensagem, chave):
    mensagem = mensagem.lower()  # Converte tudo para minúsculo
    criptografada = ''
    for letra in mensagem:
        criptografada += criptografarLetra(letra, chave)  # Usa a função de letra
    return criptografada

# Decodifica uma mensagem inteira usando uma chave fixa
def decodificarChave(mensagem, chave):
    mensagem = mensagem.lower()
    decodificada = ''
    for letra in mensagem:
        decodificada += decodificarLetra(letra, chave)
    return decodificada

# Criptografa uma mensagem usando uma chave aleatória entre 0 e 25
def criptografarAleatoria(mensagem):
    chave = randint(0, 25)  # Gera uma chave aleatória
    criptografada = criptografarChave(mensagem, chave)
    print(f"Mensagem original: {mensagem}")
    print(f"Mensagem criptografada: {criptografada}")
    print(f"Chave usada: {chave}")

# Testa todas as chaves possíveis (0 a 25) para tentar decodificar a mensagem
def decodificarSemChave(mensagem):
    mensagem = mensagem.lower()
    for chave in range(26):
        tentativa = decodificarChave(mensagem, chave)
        print(f"Chave {chave:02}: {tentativa}")  # Exibe a chave e o resultado

# Menu principal do programa
def menu():
    while True:
        # Exibe as opções para o usuário
        print("\n-=-=-=-=-=- Menu -=-=-=-=-=-")
        print("[ 1 ] Criptografar Mensagem (com chave)")
        print("[ 2 ] Decodificar Mensagem (com chave)")
        print("[ 3 ] Criptografar Mensagem (sem chave - aleatória)")
        print("[ 4 ] Decodificar Mensagem (sem chave - tentativa)")
        print("[ 5 ] Sair")

        # Recebe a opção do usuário
        opcao = input("Escolha uma opção (1-5): ")

        # Opção 1: Criptografar com chave informada
        if opcao == '1':
            mensagem = input("Digite a mensagem: ")
            chave = input("Digite a chave (0-25): ")
            if chave.isdigit():  # Verifica se é número
                chave = int(chave)
                if 0 <= chave <= 25:
                    resultado = criptografarChave(mensagem, chave)
                    print(f"Mensagem original: {mensagem}")
                    print(f"Mensagem criptografada: {resultado}")
                else:
                    print("Chave inválida. Deve estar entre 0 e 25.")
            else:
                print("Chave deve ser um número inteiro.")
        
        # Opção 2: Decodificar com chave informada
        elif opcao == '2':
            mensagem = input("Digite a mensagem criptografada: ")
            chave = input("Digite a chave (0-25): ")
            if chave.isdigit():
                chave = int(chave)
                if 0 <= chave <= 25:
                    resultado = decodificarChave(mensagem, chave)
                    print(f"Mensagem criptografada: {mensagem}")
                    print(f"Mensagem decodificada: {resultado}")
                else:
                    print("Chave inválida. Deve estar entre 0 e 25.")
            else:
                print("Chave deve ser um número inteiro.")

        # Opção 3: Criptografar com chave aleatória
        elif opcao == '3':
            mensagem = input("Digite a mensagem: ")
            criptografarAleatoria(mensagem)

        # Opção 4: Tentar decodificar sem saber a chave
        elif opcao == '4':
            mensagem = input("Digite a mensagem criptografada: ")
            decodificarSemChave(mensagem)

        # Opção 5: Encerrar o programa
        elif opcao == '5':
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida!")

        # Pergunta se o usuário quer continuar
        continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            break

# Inicia o programa chamando o menu
menu()
