#Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
#seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
cont4=0
cont3=0
cont2=0
cont1=0
i=1
while(i>0):
    n=int(input("digite um numero: "))
    if(n>=0)and(n<=25):
        cont1+=1
    if(n>=26)and(n<=50):
        cont2+=1
    if(n>=51)and(n<=75):
        cont3+=1
    if(n>=76)and(n<=100):
        cont4+=1
    if(n<0):
        i=-1
print("intervalo de 0 a 25 e",cont1)
print("intervalo de 26 a 50 e",cont2)
print("intervalo de 51 a 75 e",cont3)
print("intervalo de 76 a 100 e",cont4)