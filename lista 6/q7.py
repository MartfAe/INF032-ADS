populacao_a= 5000000
populacao_b= 7000000
taxa_a= 0.03
taxa_b= 0.02

anos = 0

while populacao_a <= populacao_b:
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    anos += 1
    
print('São necessários {} para que A ultrapasse B'.format(anos))