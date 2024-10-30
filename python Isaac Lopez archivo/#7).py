#7)Uma loja tem 150 clientes catastrados e desea mandar uma correspondencia a cada um deles anunciando um bônus especial. Escreva un
#algoritmo que leia el nombre, o endereço do cliente eo valor de sus compras y calcula un bono de 10% se o valor das
#compras por menor o igual a R$ 50.000,00 e de 15%, se superior a este valor.
for i in range(5):
    cliente=str(input("o nome do cliente: "))
    endereço=str(input("o endereço do cliente: "))
    valor=int(input("o valor da compra: "))
    if(valor>50000):
        a=(valor/10)+valor
    if(valor<=50000):
        a=(valor/15)+valor
    print("o valor teve um aumento de:",a)