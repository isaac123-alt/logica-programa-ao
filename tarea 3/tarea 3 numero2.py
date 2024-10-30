#2)Faça um Programa que pergunte quanto você ganha por hora eo número de horas trabalhadas no mês. Calcula y muestra el total de tu salario
#  no referido más.
n1=int(input("quanto voce ganha por hora: "))
n2=int(input("quantas horas voce trabalho no mes: "))
if(n1):
    print("reais por hora:",n1)
if(n2):
    print("horas trabalhadas no mes:",n2)
soma=n1*n2
print("sueldo semanal:",soma)