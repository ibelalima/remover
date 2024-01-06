lista = [0,1,2,3,4,5,6,7,8,9]
indice = int(input("qual o indice que você quer remover da lista ?"))
lista2 = []
for i in range (len(lista)):
    if i != indice:
        lista2.append(lista[i])
lista = lista2
print(lista)