#6)Escrever um algoritmo que leia 50 números e informar cuántos valores son negativos.
valor=0
for i in range(5):
    n1=int(input("digite um numero: "))
    if(n1<0):
        print("negativo")
        valor+=1
    print("numero positivo",valor)