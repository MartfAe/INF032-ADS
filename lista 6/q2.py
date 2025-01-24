count = 0

while True:
    number = int(input("Digite um número (negativo para sair): "))
    if number < 0:
        break
    count += 1

print(f"Quantidade de números digitados: {count}")