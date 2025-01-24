while True:
        nome = input("Digite um nome (ou 'FIM' para encerrar): ")

        if nome == "FIM":
            break

        if nome:
            print(f"Primeiro caractere: {nome[0]}")