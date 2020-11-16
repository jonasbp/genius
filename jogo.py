#Jogo Genius
import random
lista=[]
valor=[]
lista_cores=("Verde","Vermelho","Amarelo","Azul")
lista.append(lista_cores[random.randrange(0, 4)])
print(lista)
valor.append(input())
i=0
pont=0
while lista[i]==valor[i]:
    if i<len(lista)-1:
        i+=1
    else:
        i=0
        pont+=1
        lista.append(lista_cores[random.randrange(0, 3)])
        print(lista)
        valor=[]
        while len(lista)>len(valor):
            valor.append(input())
            if valor[i]!=lista[i]:
                break
print(pont)