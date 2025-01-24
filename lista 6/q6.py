while True:
        numero = int(input("Digite um número (ou 999 para encerrar): "))

        if numero == 999:
            break

        print(f"Divisores de {numero}: ", end="")
        for i in range(1, numero + 1):
            if numero % i == 0:
                print(i, end="")
        print()