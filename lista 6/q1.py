while True:
    num = int(input("Digite um número(999 para sair): "))
    if num == 999:
        break
    else:
        print("O triplo de {} é {}".format(num, num*3))