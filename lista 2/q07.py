qtdFitas = int(input('Digite a quantidade de fitas:'))
valorAluguel= float(input('Digite o valor do aluguel:'))

fitasAlugadas = (qtdFitas//3)
faturamentoAnual= (fitasAlugadas*valorAluguel*12)
multa = ((fitasAlugadas*0.1)*(valorAluguel*0.1))

fitasEstragadas = (qtdFitas*0.02)
fitasRepostas = (qtdFitas*0.1)
fitasFinais = qtdFitas-fitasEstragadas+fitasRepostas

print(f'O faturamento anual é de R$ {faturamentoAnual:.2f} ')
print(f'O valor ganho de multa por mês é R$ {multa:.2f}')
print(f'O número de fitas que restaram é {fitasFinais:.0f}')
