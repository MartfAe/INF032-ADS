numeros = []

for i in range(10):
    while True:
        numero = int(input(f'Digite o {i+1}º número (deve ser >0): '))
        if numero >= 0:
            numeros.append(numero)
            break
        else:
            print("Número inválido. Digite novamente.")

print('Os números digitados foram:', numeros)