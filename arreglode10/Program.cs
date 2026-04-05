using System;

int[] misNumeros = new int[10];


misNumeros[0] = 100; 
misNumeros[9] = 900; 

Console.WriteLine("El primer número es: " + misNumeros[0]);

// Esto evita que la consola se cierre sola inmediatamente
Console.WriteLine("Presiona cualquier tecla para salir...");
Console.ReadKey();