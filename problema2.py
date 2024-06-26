#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)

t = input().split()
t_inversa = tuple(reversed(t))

resultado = []
for elemento in t_inversa:
    if elemento.isdigit():
        resultado.append(elemento)
    else:
        resultado.append(f"'{elemento}'")
if len(resultado) == 1:
    print("(", resultado[0], ",)", sep="")
else:
    print("(", ", ".join(resultado), ")", sep="")
