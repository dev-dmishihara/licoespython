# laços de repetição / listas
# Problema 1 a N - Imprima na tela os valores de 1 a N
'''
input numero_maximo
valor inicial = 1
loop de valor inicial a numero_maximo
    print valor
'''
valor_maximo = input('Digite o valor máximo: ')
valor_inicial = 1
for numero in range(valor_inicial, int(valor_maximo) + 1):
    print(numero)