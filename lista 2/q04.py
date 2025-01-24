valorHoraAula = float(input("Digite o valor da hora aula: "))
numeroAulas = int(input("Digite o número de aulas dadas: "))
desconto = float(input("Digite o percentual de desconto: "))

salarioBruto = valorHoraAula * numeroAulas
salarioLiquido = salarioBruto - (salarioBruto * desconto / 100)
print('Salario líquido é de :', salarioLiquido, 'reais.')