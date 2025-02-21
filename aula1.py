# Variaveis

# Números
velocidade_internet = 10
print (velocidade_internet)
nota_filme = 8.5 # float
# valores boleanos
esta_aberto = True
# Strings
nome_do_curso = "Lógica de Programação"

# Como variáveis seriam usadas em um problema real?
# PROBLEMA 1 - Valor por Hora "Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas em um mês."
'''
input salario_mensal
input horas_trabalhadas_no_mes
valor_hora = salario_mensal / horas_trabalhadas_no_mes
print valor_hora
'''
salario_mensal = input ('Qual é o seu salário mensal?')
horas_trabalhadas = input ('Quantas horas trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas)
print (valor_hora)
