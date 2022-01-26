import math

lista = [3,4,8,5,5,22,13]

def buscar(lista):
    for x in range (2,int(math.sqrt(lista)) + 1):
        if lista % x == 0:
            return False
    return True

print (list(filter(buscar,lista)))