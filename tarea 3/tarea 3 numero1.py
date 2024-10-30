#1) Tendo como dado de entrada a altura (h) de una persona, construye un algoritmo que calcula tu peso ideal, utilizando como siguientes fórmulas:
#Para hombres: (72.7*h) - 58
#Para mujeres: (62,1*h) - 44,7
H=int(input("informe um peso ideal: "))
hombres=(72.7*H-58) 
mulheres=(62.1*H-44.7) 
print("seu peso ideal de hombre e",hombres)
print("seu peso ideal de mulher e",mulheres)