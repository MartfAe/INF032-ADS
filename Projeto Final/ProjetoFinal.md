# Projeto: Estação Meteorológica com Display de 7 Segmentos e Python

**Dupla:** Ana Emília Lobo e Anna Luisa Santos

## Objetivo
O projeto tem como finalidade criar uma estação meteorológica capaz de medir e exibir a temperatura ambiente em um display de 7 segmentos, ao mesmo tempo em que utiliza Python para registrar e visualizar as mudanças de temperatura em gráficos. Essa abordagem integra conceitos de eletrônica, programação embarcada e análise de dados.

## Descrição do Funcionamento
1. Um sensor de temperatura (DHT11) mede a temperatura do ambiente.
2. O Arduino processa os dados e exibe o valor no display de 7 segmentos, alternando entre os dígitos para números com mais de um dígito.
3. Simultaneamente, os dados são enviados via comunicação serial para um script Python que:
   - Registra os valores em tempo real.
   - Cria um gráfico dinâmico que acompanha as variações de temperatura ao longo do tempo.

## Componentes Utilizados
- **Sensor de temperatura:** DHT11  
- **Display de 7 segmentos:** Anodo comum ou com driver. 
- **Outros componentes:** Resistores para proteção dos pinos do display  
- **Microcontrolador:** Arduino Uno  
- **Software:** Python para processamento e visualização de dados  

## Destaques Técnicos
- **Exibição Local:** O display de 7 segmentos mostra a temperatura ambiente em tempo real, com atualização regular a cada 2 segundos.  
- **Integração com Python:** A comunicação serial permite enviar os dados do Arduino para o Python, onde são registrados e visualizados por meio de gráficos dinâmicos com o uso de uma biblioteca. 
- **Simplicidade e Expansibilidade:** O projeto é modular e pode ser expandido para incluir outras funcionalidades, como monitoramento de umidade, alertas visuais ou armazenamento de dados.  

## Possíveis Expansões
- Adicionar um botão ao Arduino para alternar entre exibir temperatura e umidade no display.  
- Incorporar Python para armazenar dados em um banco de dados ou arquivo CSV para análises posteriores.  
