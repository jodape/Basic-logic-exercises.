""""

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

"""
"""
for i in range (0, 100):
    print(i)
    if (i % 3) == 0:
        print ("Fizz")
    elif (i % 5) == 0:
        print ("Buzz")
    elif (i % 5) == 0 and (i% 3) == 0:
        print ("Fizzbuzz")
"""
#VERSIÓN CON CORRECCIÓN
"""
#1 a 100
for i in range(1,101):
    
    #Primero evaluamos si es múltiplo de 5 y de 3
    if i % 3 == 0 and i % 5 == 0:

        print("fizzbuzz") 

    #Si no es múltiplo de 5 y de 3, entonces evaluaremos para 3
    elif i % 3 == 0:

        print("fizz")

    #Evalúa si es múltiplo de 5
    elif i % 5 == 0:
        
        print("buzz")

    #Sino es múltiplo de ninguno, imprime el número normal.    
    else:
        print(i)

"""
#Otra versión: 

for i in range (1,101):
    divisible_by_three = i % 3 == 0
    divisible_by_five = i % 5 == 0
    
    if divisible_by_three & divisible_by_three:
        print("fizzbuzz")
    elif divisible_by_three:
        print("fizz")
    elif divisible_by_five:
        print("buzz")
    else:
        print(i)



