#5)Faça um algoritmo
#que receba o peso, a idade e a altura de cem pessoas, calcule e informe os valores de: maior peso, menor peso, maior
#altura, menor altura, maior idade e menor idade deste grupo de pessoas.
maior=0
maior2=0
maior3=0
menor=0
menor2=0
menor3=0
for i in range(10):
    idade=int(input("digite uma idade: "))
    altura=int(input("digite uma altura: "))
    peso=int(input("digite um peso: "))
    if(i==1):
        maior=idade
        maior2=peso
        maior3=altura
        menor=idade
        menor2=peso
        menor3=altura
    else:
        if(idade>maior):
            maior=idade
        if(peso>maior2):
            maior2=peso
        if(altura>maior3):
            maior3=altura
        if(idade<menor):
            menor=idade
        if(peso<menor2):
            menor2=peso
        if(altura<menor3):
            menor3=altura
print("a maior idade foi",maior)
print("o maior peso foi",maior2)
print("a maior altura foi",maior3)
print("a menor idade foi",menor)
print("o menor peso foi",menor2)
print("a menor altura foi",menor3)