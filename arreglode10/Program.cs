using System;
class Program
{
    static void Main()
    {
        int[] arreglo = new int[10];
        arreglo[0] = 100;
        arreglo[1] = 900;

        Random generador = new Random();

        for (int i = 2; i < arreglo.Length; i++)
        {
            arreglo[i] = generador.Next(1, 101);
        }

        Console.WriteLine("Iniciando el recorrido del arreglo...");
       

        for (int i = 0; i < arreglo.Length; i++)
        {
            Console.WriteLine($"Indice [" + i + "]:" + arreglo[i]);
        }

        Console.WriteLine("Precina cualquier tecla para salir.... ");
        Console.ReadKey();

    }
}