chico = 1.5
juca = 1.1
taxaChico = 0.02
taxaJuca = 0.03

anos = 0 

while juca <=chico:
    chico += taxaChico
    juca += taxaJuca
    anos += 1

print('São necessários {} anos para que Juca ultrapasse Chico'.format(anos))