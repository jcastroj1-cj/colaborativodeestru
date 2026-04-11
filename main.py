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