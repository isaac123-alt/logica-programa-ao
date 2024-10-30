#9)Faça um algoritmo que receba o tamanho de 500 camisetas existentes no almoxarifado e ao final informe quantas camisetas de cada tamanho P, M, G, GG.
cont=0
cont1=0
cont2=0
cont3=0
for i in range(10):
    ropa=str(input("qual e o tamanho da camiseta: "))
    if(ropa=="P"):
        cont+=1
    elif(ropa=="M"):
        cont1+=1
    elif(ropa=="G"):
        cont2+=1
    elif(ropa=="GG"):
        cont3+=1
print("roupas P",cont)
print("roupas M",cont1)
print("roupas G",cont2)
print("roupas GG",cont3)