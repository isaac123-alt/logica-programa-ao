#2)Construya un algoritmo que leia cem números y mostre qual o maior número que foi lido.
soma=0
for i in range(1,5):
    n1=int(input("digite um numero: "))
    if(n1>soma):
        soma=n1
print(soma)