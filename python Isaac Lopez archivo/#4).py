#4)Escreva un algoritmo que recibe 100 números, y cuenta cuántos de ellos están en el intervalo [10, 20] 
# y cuántos de ellos están en el intervalo, escribiendo estas informaciones.
dentro=0
fora=0
for i in range(5):
    valor=int(input("digite um valor: "))
    if(10<=valor<=20):
        dentro+=1
    else:
        fora+=1
print("numeros no intervalo:",dentro)
print("numeros fora do intervalo:",fora)