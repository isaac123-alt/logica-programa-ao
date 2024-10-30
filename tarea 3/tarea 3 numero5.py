#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo es aquele
#  que é divisível somente por ele mesmo e por 1.
n1=int(input("informe um numero: "))
if(n1>1):
    for i in range(2,n1):
        if(n1%i==0):
            print("nao e um numero primo")
            break
        else:
            print("e um numero primo")
            break
else:
    print("nao e um numero primo")