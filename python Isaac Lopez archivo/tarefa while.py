#1.FAÇA UM PROGRAMA QUE RECEBA A IDADE, ALTURA E O PESO DE 25 PESSOAS E MOSTRE:A QUANTIDADE DE PESSOAS COM IDADE SUPERIOR A 50 ANOS.
contador=0
idade=0
while(idade<3):
    idade+=1
    idade1=int(input("imforme sua idade: "))
    idade2=int(input("informe a sua altura: "))
    idade3=int(input("informe o seu peso: "))
    if(idade1>50):
        contador+=1
    else:
        idade=idade
print("pessoas superiores a 50 anos:",contador)