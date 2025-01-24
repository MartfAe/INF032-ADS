 tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ").strip()
quantidade = float(input("Digite a quantidade de carne em Kg: "))
forma_pagamento = input("Digite a forma de pagamento (dinheiro ou cartão Tabajara): ").strip().lower()

if tipo_carne == "File Duplo":
    if quantidade <= 5:
        preco_total = 4.90 * quantidade
    else:
        preco_total = 5.80 * quantidade
elif tipo_carne == "Alcatra":
    if quantidade <= 5:
        preco_total = 5.90 * quantidade
    else:
        preco_total = 6.80 * quantidade
elif tipo_carne == "Picanha":
    if quantidade <= 5:
        preco_total = 6.90 * quantidade
    else:
        preco_total = 7.80 * quantidade
else:
    print("Tipo de carne inválido!")
    return

if forma_pagamento == "cartão tabajara":
    desconto = preco_total * 0.05  # 5% de desconto
    valor_a_pagar = preco_total - desconto
else:
    desconto = 0
    valor_a_pagar = preco_total
    
print("\nCupom Fiscal:")
print(f"Tipo de Carne: {tipo_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço Total: R$ {preco_total:.2f}")
if desconto > 0:
    print(f"Desconto (5% no Cartão Tabajara): R$ {desconto:.2f}")
print(f"Valor a Pagar: R$ {valor_a_pagar:.2f}")