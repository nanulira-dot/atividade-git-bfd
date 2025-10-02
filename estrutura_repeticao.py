# Objetivo: somar números pares de 1 a 10
pares = []  # lista para armazenar números pares

# Usando for para percorrer números de 1 a 10
for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)  # adiciona números pares à lista

print("Números pares de 1 a 10:", pares)

# While para calcular a soma desses números pares
soma = 0
index = 0
while index < len(pares):   # enquanto o índice for menor que o tamanho da lista
    soma += pares[index]    # adiciona o valor da posição atual à soma
    index += 1              # passa para o próximo índice

print("Soma dos números pares é:", soma)