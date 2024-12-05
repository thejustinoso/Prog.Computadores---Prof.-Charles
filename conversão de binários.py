#conversão em binários

numeroDec = int(input('Digite um número inteiro'))

for i in range (numeroDec, -1):
    restoDivisao = numeroDec % 2
    numeroBin = restoDivisao
    if numeroDec <= 0:
        break 

    print(f'O número decimal {numeroDec} convertido para número binário fica: {numeroBin}.')
