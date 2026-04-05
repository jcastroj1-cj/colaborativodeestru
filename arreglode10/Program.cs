using System;

class Program
{
    static void Main()
    {
        // 1. Declaración y llenado
        int[] arreglo = new int[10];
        arreglo[0] = 100;
        arreglo[1] = 901;

        Random generador = new Random();
        for (int i = 2; i < arreglo.Length; i++)
        {
            arreglo[i] = generador.Next(1, 101);
        }

        
        Console.WriteLine("Arreglo original (con impares):");
        ImprimirArreglo(arreglo);

        // Cambiar impares por cero
        for (int i = 0; i < arreglo.Length; i++)
        {
            if (arreglo[i] % 2 != 0)
            {
                arreglo[i] = 0;
            }
        }

        
        Console.WriteLine("\nArreglo modificado (impares reemplazados por 0):");
        ImprimirArreglo(arreglo);

        Console.WriteLine("\nPresiona cualquier tecla para salir.... ");
        Console.ReadKey();
    } 

    static void ImprimirArreglo(int[] arr)
    {
        foreach (int n in arr)
        {
            Console.Write(n + " ");
        }
        Console.WriteLine();
    }
} 