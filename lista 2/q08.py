
numeroConta = int(input("Digite o número da conta: "))
if len(numeroConta)>3 or len(numeroConta)<3:
    print("Número da conta inválido")
    return
else:
    numeroInvertido = numeroConta[::-1]
    digitoVerificador = (numeroConta + numeroInvertido)
    
