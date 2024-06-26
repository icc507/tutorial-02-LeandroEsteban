#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t1 = tuple(input().split())
t2 = tuple(input().split())
union = t2 + t1 + t2

resultado = []
for elemento in union:
    if elemento.isdigit():
        resultado.append(elemento)
    else:
        resultado.append(f"'{elemento}'")

print("(", ", ".join(resultado), ")", sep="")