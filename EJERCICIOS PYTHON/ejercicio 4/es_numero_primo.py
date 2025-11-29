"""
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""

i = 0
primo = True

for j in range(2, 100):   # empezamos en 2 porque 0 y 1 no son primos
    primo = True           # reiniciamos para cada número
    
    for i in range(2, j):
        if j % i == 0:
            print(j, "no es primo,", i, "es divisor")
            primo = False
            break
    
    if primo:
        print(j, "es primo")
