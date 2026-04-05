using System;

class Program
{
    static void Main()
    {
        // 1. Declarar el arreglo de 10 enteros
        int[] arreglo = new int[10];

        // 2. Llenado inicial (usaremos aleatorios para probar)
        Random generador = new Random();
        for (int i = 0; i < arreglo.Length; i++)
        {
            arreglo[i] = generador.Next(1, 11); // Números del 1 al 10
        }

        Console.WriteLine("--- Arreglo Inicial ---");
        ImprimirArreglo(arreglo);

        // 3. PROCESO: Multiplicar cada valor por su índice (posición)
        for (int i = 0; i < arreglo.Length; i++)
        {
            // Tomamos el número y lo multiplicamos por 'i' (0, 1, 2...)
            arreglo[i] = arreglo[i] * i;
        }

        Console.WriteLine("\n--- Arreglo multiplicado por su indice ---");
        ImprimirArreglo(arreglo);

        Console.WriteLine("\nPresiona cualquier tecla para salir...");
        Console.ReadKey();
    }

    // Método para imprimir los valores
    static void ImprimirArreglo(int[] arr)
    {
        foreach (int n in arr)
        {
            Console.Write(n + " ");
        }
        Console.WriteLine();
    }
}