import sys

numero = int(input('Informe um valor:'))

contador = 1
fatorial = 1

if numero < 0:
    SystemExit
    print('Informe um número positivo')

else:
    while contador <= numero:
        fatorial *= contador
        contador += 1 
    print (f'{numero}! = {fatorial}')
