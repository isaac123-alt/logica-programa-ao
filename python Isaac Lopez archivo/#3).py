#3)Construir un algoritmo que receba cem números e informe a medio e a soma entre los números positivos.
soma=0
soma1=0
for i in range(10):
    valor=int(input("digite um valor: "))
    if(valor>0):
        soma+=valor
        soma1+=1
    if(soma1>0):
        media=soma/soma1
    else:
        media=0
print("soma dos numeros:",soma)
print("media dos numeros:",media)