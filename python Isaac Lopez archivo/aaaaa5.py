#5) Crie um algoritmo que leia um número inteiro. Se o número lido for positivo, escreva uma mensagem indicando se ele e par ou impar.
n1=int(input("digite um numero inteiro: "))
if(n1>=0):
    print("e positivo")
    if(n1%2==0):
     print("o numero e par")
    else:
     print("o numero e impar")
else:
   print("valor e negativo")