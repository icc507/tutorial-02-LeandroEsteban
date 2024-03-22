def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if arbol == []:
        arbol += arbolTrinario(numero)
    else:
        if numero < arbol[0]:
            insertaEnArbolTrinario(arbol[1], numero)
        elif numero > arbol[0]:
            insertaEnArbolTrinario(arbol[3], numero)
        else:
            if isinstance(arbol[2], list):
                insertaEnArbolTrinario(arbol[2], numero)
            else:
                arbol[2] = [arbol[2], [numero, [], [], []], []]

entrada = input()
numeros = list(map(int, entrada.split()))

arbol = []
for num in numeros:
    insertaEnArbolTrinario(arbol, num)

print(arbol)



