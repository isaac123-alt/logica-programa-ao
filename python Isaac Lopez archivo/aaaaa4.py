#Construa um algoritmo que receba o código e o total de vendas do vendedor, 
# calcule a comissão conforme a tabela e informe o código e a comissão do vendedor:
n1=int(input("digite o codigo do vendedor: "))
totalvendas=float(input("digite o codigo total de vendas: "))
if(totalvendas<100):
   print("a comisao aumento 0%")
elif(totalvendas>100)and(totalvendas<350):
    print('comissao aumento 6%')
    soma=(totalvendas/6)+totalvendas
    print(soma)
elif(totalvendas>350):
    print("a comisao aumentou 10%")
    soma=(totalvendas/10)+totalvendas
    print(soma)