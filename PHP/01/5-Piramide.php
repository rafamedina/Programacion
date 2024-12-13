<?php
/** 
Ejercicio 5: Pirámide de Números
Objetivo: Imprimir una pirámide de números utilizando bucles anidados.
Pasos:
Pedir al usuario que ingrese la altura de la pirámide.
Utilizar dos bucles anidados para imprimir los números en forma de pirámide.
Consejos adicionales:
Comentarios: Utiliza comentarios para explicar tu código y hacerlo más legible.
Indentación: Indenta tu código correctamente para mejorar su estructura y legibilidad.
Variables descriptivas: Utiliza nombres de variables que describan su propósito.
Funciones: Si tu código se vuelve demasiado largo, puedes crear funciones para organizar mejor el código y reutilizarlo.
*/

// Pedir al usuario que ingrese la altura de la pirámide

$altura = readline("Ingrese la altura de la pirámide: ");
// Función para imprimir la pirámide de números
    // Bucle externo para controlar la altura de la pirámide
    for ($i = 1; $i <= $altura; $i++) {
        // Bucle interno para imprimir los números en cada fila
        for ($x = 1; $x <= $i; $x++) {
            // Imprimir el número actual
            echo $x . " ";
        }
        // Salto de línea para pasar a la siguiente fila
        echo "\n";
    }

// Llamar a la función para imprimir la pirámide
