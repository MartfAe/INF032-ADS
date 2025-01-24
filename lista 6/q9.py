
total_residencial = 0
qtd_residencial = 0
total_comercial = 0
qtd_comercial = 0
total_industrial = 0
qtd_industrial = 0

print("Digite os dados dos consumidores (número 0 para encerrar):")

while True:
    
    numero_consumidor = int(input("Número do consumidor: "))
    if numero_consumidor == 0:
        break

    kwh_consumidos = float(input("Quantidade de kWh consumidos no mês: "))
    tipo_consumidor = int(input("Tipo do consumidor (1-Residencial, 2-Comercial, 3-Industrial): "))

    
    if tipo_consumidor == 1:
        custo = kwh_consumidos * 0.3
        total_residencial += kwh_consumidos
        qtd_residencial += 1
    elif tipo_consumidor == 2:
        custo = kwh_consumidos * 0.5
        total_comercial += kwh_consumidos
        qtd_comercial += 1
    elif tipo_consumidor == 3:
        custo = kwh_consumidos * 0.7
        total_industrial += kwh_consumidos
        qtd_industrial += 1
    else:
        print("Tipo de consumidor inválido. Tente novamente.")
        continue

  
    print(f"Custo total para o consumidor {numero_consumidor}: R$ {custo:.2f}\n")


media_residencial = total_residencial / qtd_residencial if qtd_residencial > 0 else 0
media_comercial = total_comercial / qtd_comercial if qtd_comercial > 0 else 0

print("Resultados Finais:")
print(f"Total de consumo para consumidores residenciais: {total_residencial:.2f} kWh")
print(f"Total de consumo para consumidores comerciais: {total_comercial:.2f} kWh")
print(f"Total de consumo para consumidores industriais: {total_industrial:.2f} kWh")
print(f"Média de consumo para consumidores residenciais: {media_residencial:.2f} kWh")
print(f"Média de consumo para consumidores comerciais: {media_comercial:.2f} kWh")
