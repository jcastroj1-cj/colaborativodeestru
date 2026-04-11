import random

# Arreglo de 10 enteros con valores aleatorios
arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo:", arreglo)
# Bucle for clásico (con índice)
print("\n--- For clásico ---")
for i in range(len(arreglo)):
    print(f"arreglo[{i}] = {arreglo[i]}")

#blucle for each
print("\n--- For-each ---")
for elemento in arreglo:
    print(elemento)

for i in range(len(arreglo)):
    if arreglo[i] % 2 != 0:
        arreglo[i] = 0

print("\nArreglo con impares en cero:", arreglo)

# Multiplicar todos los valores por su índice
for i in range(len(arreglo)):
    arreglo[i] = arreglo[i] * i

print("Arreglo multiplicado por índice:", arreglo)