#Faça um programa que leia e valide as seguintes informações:
#Nombre: más de 3 caracteres;
#Ida: entre 0 y 150;
#Salario: mayor que cero;
#Sexo: 'f' o 'm';
#Estado Civil: 's', 'c', 'v', 'd';
nome=str(input("informe um nome: "))
nome2=len(nome)
if(nome2<=3):
    print("valido")
else:
    print("invalido")
idade=int(input("informe uma idade: "))
if(idade>=0)and(idade<=150):
    print("valido",)
else:
    print("invalido")
salario=int(input("informe um salario: "))
if(salario>0):
    print("valido",)
else:
    print("invalido")
sexo=str(input("informe seu sexo: "))
if(sexo=="f")or(sexo=="m"):
    print("valido")
else:
    print("invalido")
estadocivil=str(input("informe seu estado civil: "))
if(estadocivil=="s")or(estadocivil=="c")or(estadocivil=="v")or(estadocivil=="d"):
   print("valido")
else:
    print("invalido")