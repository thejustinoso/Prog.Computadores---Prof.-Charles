import sys

valor = int(input('Digite um valor para ser expresso na sequência de Fibonacci:'))

if valor <= 0:
    SystemExit
    print('Informe um número positivo')
    
else:
    anterior, atual = 0, 1
    contador = 1 
    
    while contador <= valor:
        print(atual)
        anterior, atual = atual, atual + anterior
        contador += 1
