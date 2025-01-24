count = 0
soma = 0

while True:
    nota = input('Digite a nota do aluno (ou "fim" para sair): ')
    if nota == "fim":
        break
    else:
        count += 1
        soma += float(nota)
        media = soma / count
        print(media)
