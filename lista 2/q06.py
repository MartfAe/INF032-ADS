emprestimo = float(input('Digite o valor do emprestimo: '))
meses = int(input('Digite a quantidade de meses: '))
juros = float(input('Digite o percentual de juros: '))

parcela = (emprestimo*(juros/100+1)) / meses

print('Valor da parcela:', parcela)