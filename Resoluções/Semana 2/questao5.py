# Peço ao usuário o tamanho do arquivo e sua velocidade de conexão:
tamanho = float(input('Qual o tamanho do arquivo em megabytes(MB)?\n'))
velocidade_conexao = float(input('Qual a velocidade de sua Conexão (em Mbps)?\n'))

# Para calcular a velocidade de download em mbps, divido o tamanho pela velocidade de conexão:
velocidade = tamanho / velocidade_conexao

# Formato para segundos ao multiplicar por 8:
velocidadePorMega = velocidade * 8

# Mostro ao usuário o tempo estimado de download:
print(f'O tempo estimado de download é de{velocidadePorMega: .2f} segundos.')

# Realizo uma verificação para descobrir se a velocidade é rápida
print(f'Download rápido? {velocidadePorMega <= 60}')