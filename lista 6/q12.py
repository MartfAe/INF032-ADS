area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

areaFolga = area * 1.1  

quantidadeTinta = areaFolga/6

latas = (quantidadeTinta +17) // 18
precoLatas = latas * 80

galoes = (quantidadeTinta + 3.5) // 3.6
precoGaloes = galoes * 25

latas_mistura = quantidade_tinta // 18  
tinta_restante = quantidade_tinta - latas_mistura * 18  
galoes_mistura = (tinta_restante + 3.5) // 3.6 
preco_mistura = latas_mistura * 80 + galoes_mistura * 25  


print(f"\nResultado para a área de {area} m² (com 10% de folga):\n")
print(f"1. Comprar apenas latas de 18 litros:")
print(f"   Quantidade de latas: {int(latas)} latas")
print(f"   Preço total: R$ {preco_latas:.2f}")
print()

print(f"2. Comprar apenas galões de 3,6 litros:")
print(f"   Quantidade de galões: {int(galoes)} galões")
print(f"   Preço total: R$ {preco_galoes:.2f}")
print()

print(f"3. Misturar latas e galões para o menor preço:")
print(f"   Quantidade de latas: {int(latas_mistura)} latas")
print(f"   Quantidade de galões: {int(galoes_mistura)} galões")
print(f"   Preço total: R$ {preco_mistura:.2f}")