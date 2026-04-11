matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t ")
    print()

print("\nRecorrido por columnas:")
for col in range(3):
    for fila in range(3):
        print(f"matriz[{fila}][{col}] = {matriz[fila][col]}")
    print()

    # Sumar todos los elementos
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento

    print(f"Suma de todos los elementos: {total}")
