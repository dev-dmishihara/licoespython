# Condicionais
valor1 = input ('Digite o primeiro valor: ') # <- Solicito o primeiro valor
valor2 = input ('Digite o segundo valor: ')# <- Solicito o segundo valor

if int(valor1) > int(valor2): #<- aqui é colocado a condição if, que faz a comparação valor1 é maior que valor2? Caso sim, a primeira condição é atendida e mostra na tela a mensagem abaixo.
    print ("O primeiro valor é maior.")
else: #<- Caso a primeira comparação não seja verdadeira, ela continua analisando a próxima condição que é senão, ou seja se a primeira condição não e cumprida, vamos apresentar a segunda. 
    print ("O segundo valor é maior.")