# 1. Solicita os 4 números via input e os armazena em uma lista
numeros = []
for i in range(1, 5):
    valor = input(f"Digite o {i}º número: ")
    # 2. Converte cada valor recebido para float
    numeros.append(float(valor))

# 3. Calcula a média somando os itens da lista e dividindo pela quantidade
media = sum(numeros) / len(numeros)

# 4. Exibe o resultado com duas casas decimais usando f-string
print(f"A média dos números informados é: {media:.2f}")
