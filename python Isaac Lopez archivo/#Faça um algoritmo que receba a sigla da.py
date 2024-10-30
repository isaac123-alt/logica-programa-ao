#Faça um algoritmo que receba a sigla da cidade de origem de um grupo de personas, ao informe final quantas foram digitadas das cidades do Rio de Janeiro
# , Belo Horizonte e Santa Catarina (por separado).
#  El algoritmo se cierra cuando se digitaliza la palabra “fim”.
i=0
rj=0
bh=0
sc=0
while(i<1):
    sigla=str(input("informe uma sigla: "))
    if sigla=="rj":
        rj+=1
    if sigla=="bh":
        bh+=1
    if sigla=="sc":
        sc+=1
    if sigla=="fim":
        i=2
print("pessoas de rio de janeiro",rj)
print("pessoas de belo horizonte",bh)
print("pessoas de santa catarina",sc)
