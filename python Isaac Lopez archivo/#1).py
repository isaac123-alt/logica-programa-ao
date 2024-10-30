#1)Construya un algoritmo que reciba cinco números y muestre en medios dos números que foram digitados.
soma=0
for i in range(5):
    valor=int(input("digite um valor: "))
    soma=soma+valor
media=soma/i
print(media)