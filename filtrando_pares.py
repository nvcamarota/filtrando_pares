"""
FILTRANDO NÚMEROS PARES
Objetivo:
Introducir la comprensión de listas y el uso de for con range.

Descripción:
• El programa genera una lista de números del 1 al 20 usando range.
• Usa comprensión de listas para filtrar los números pares.
• Permite a las estudiantes imprimir los números pares o detener el programa usando break.
"""

# Números dentro de un rango del 0 al 20 como argumento de la variable «numbers»
numbers = range(0, 21)

# Listando y filtrando los números pares de la variable «numbers» en la variable «even_numbers»
even_numbers = [number for number in numbers if number % 2 == 0]

# Recorriendo los números de la variable «even_numbers» para imprimirlos hasta llegar al último número de la variable «numbers»
for number in even_numbers:
    print(number)
    next_step = input(f"¿Desea continuar con los números después del {number}?\n(Escriba «S» para confirmar. Para salir del programa, presione cualquier tecla):\n").capitalize()
    if next_step != "S":
        print("Saliendo del programa...\n¡Adiós!")
        break