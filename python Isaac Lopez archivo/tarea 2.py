#2) Em uma eleição presidencial existen quatro candidatos. Los votos están informados por
#medio de código. Los códigos utilizados son: 1, 2, 3, 4 - Votos para los respectivos candidatos (você deve montar una tabla 
#ex: 1 - Jose/ 2- João /3 - Maria/ 4 - Meu nego) 5 - Voto Nulo 6 - Voto em Branco
#Faça um programa que calcula e mostre:
#- O total de votos para cada candidato;
#- O total de votos nulos;
#- El total de votos en blanco;
#Un porcentaje de votos nulos sobre o total de votos;Un porcentaje de votos en blanco sobre el total de votos. 
#Para finalizar o algoritmo, o valor digitado debe ser igual a 0.
total=0
i=0
jose=0
joao=0
maria=0
meunego=0
votonulo=0
votobranco=0
while(i<6):
    candidato=int(input("informe um candidato: "))
    if(candidato==1):
        jose+=1
    if(candidato==2):
        joao+=1
    if(candidato==3):
        maria+=1
    if(candidato==4):
        meunego+=1
    if(candidato==5):
        votonulo+=1
    if(candidato==6):
        votobranco+=1
    if(candidato>=7):
        print("invalido")
total=jose+joao+maria+meunego
print("o total de votos para jose",jose)
print("o total de votos para joao",joao)
print("o total de votos para maria",maria)
print("o total de votos para meunego",meunego)
print("o total de votos para brancos",votobranco)
print("o total de votos para nulos",votonulo)