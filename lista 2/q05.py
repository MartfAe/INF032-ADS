consumo = 12
velocidade = int(input("Digite a velocidade do veículo: "))
tempo = float(input("Digite o tempo de viagem em horas: "))

distancia = tempo * velocidade
litrosGastos = distancia / consumo
velocidadeMedia = distancia / tempo

print('Tempo de viagem:', tempo, 'horas')
print('Velocidade média:', velocidadeMedia, 'km/h')
print('Distância percorrida:', distancia, 'km')
print('Litros gastos:', litrosGastos, 'litros')



