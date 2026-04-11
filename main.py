import random

# Arreglo de 10 enteros con valores aleatorios
arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo:", arreglo)

#blucle for clasico
print("\n--- for clasico---")
for i in range(len(arreglo)):
    print(f"arreglo{[i]}) = {arreglo[i]}")
    