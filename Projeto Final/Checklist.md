# Checklist para o Projeto: Estação Meteorológica

## Estrutura do Projeto
- [ ] Configurar o repositório no GitHub
- [ ] Criar estrutura básica de diretórios:
  - [ ] Código Arduino
  - [ ] Código Python
  - [ ] Documentação

## Desenvolvimento Arduino
- [ ] Conectar e testar o sensor de temperatura (DHT11)
- [ ] Conectar e testar o display de 7 segmentos
- [ ] Programar a exibição da temperatura no display
- [ ] Implementar a comunicação serial com Python

## Desenvolvimento Python
- [ ] Configurar comunicação serial para receber dados do Arduino
- [ ] Armazenar dados:
  - [ ] Criar arquivo CSV
  - [ ] (Opcional) Configurar banco de dados SQLite
- [ ] Implementar cálculos:
  - [ ] Média diária, semanal e mensal
  - [ ] Temperatura máxima e mínima
- [ ] Criar gráficos para acompanhar mudanças de temperatura

## Testes e Integração
- [ ] Testar integração Arduino + Python
- [ ] Validar armazenamento de dados e cálculos estatísticos
- [ ] Testar exibição de gráficos

## Documentação
- [ ] Adicionar descrição do projeto no `README.md`
- [ ] Criar instruções de uso
- [ ] Adicionar imagens ou diagramas do circuito
- [ ] Subir todos os arquivos para o GitHub