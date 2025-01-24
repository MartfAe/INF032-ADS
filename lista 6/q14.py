precoAlcool = 1.9
precoGasolina = 2.5

litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()
if tipo == "A":  # Álcool
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    preco_litro = preco_alcool

elif tipo == "G":  # Gasolina
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    preco_litro = preco_gasolina

else:
    print("Tipo de combustível inválido!")
    exit()
    
valor_bruto = litros * preco_litro
desconto_total = valor_bruto * desconto
valor_final = valor_bruto - desconto_total
print(f"Valor a ser pago: R$ {valor_final:.2f}")
