count =0

while True:
    num = int(input("Digite um número (0 para sair):"))
    if num ==0:
        break
    if 100 <=num <=200:
        count +=1
        print (count)