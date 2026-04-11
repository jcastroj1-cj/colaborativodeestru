import random

# Arreglo de 10 enteros con valores aleatorios
arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo original:", arreglo)

# Bucle for clásico (con índice)
print("\n--- For clásico ---")
for i in range(len(arreglo)):
    print(f"arreglo[{i}] = {arreglo[i]}")

# For-each equivalente en Python
print("\n--- For-each ---")
for elemento in arreglo:
    print(elemento)

# Cambiar todos los valores impares por cero
for i in range(len(arreglo)):
    if arreglo[i] % 2 != 0:
        arreglo[i] = 0

print("\nArreglo con impares en cero:", arreglo)

# Multiplicar todos los valores por su índice
for i in range(len(arreglo)):
    arreglo[i] = arreglo[i] * i
print("Arreglo multiplicado por índice:", arreglo)

def busqueda_lineal(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1

valor_buscar = int(input("\n¿Qué valor deseas buscar? "))
resultado = busqueda_lineal(arreglo, valor_buscar)

if resultado != -1:
    print(f"Valor {valor_buscar} encontrado en el índice {resultado}")
else:
    print(f"Valor {valor_buscar} no encontrado en el arreglo")