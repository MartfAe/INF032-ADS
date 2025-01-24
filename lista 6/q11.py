peso = float(input("Digite o peso dos peixes em quilos: "))
if peso > 50:
    excesso = peso - 50  
    multa = excesso * 4  
    print(f"Peso dos peixes: {peso} kg")
    print(f"Excesso de {excesso} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print(f"Peso dos peixes: {peso} kg")
    print("Não há excesso. Não há multa.")
    