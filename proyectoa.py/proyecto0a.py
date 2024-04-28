def sumarlistas(lista1, lista2):
    suma = []
    for i in range(len(lista1)):
        suma.append(lista1[i]+ lista2[i])
    return suma
listaspares =[2,4,6,8,10]
listaimpares = [1,3,5,7,9]
print(sumarlistas(listaspares,listaimpares))
