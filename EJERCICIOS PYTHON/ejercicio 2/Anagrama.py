"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

"""
"""
palabra1 = input("Primera palabra: ")
palabra2 = input("Segunda palabra: ")


#forma de reemplazar al len
long1 = 0
for _ in palabra1:
    long1 + 1

long2 = 0
for _ in palabra2:
    long2 + 1

#comparamos primero si ambos poseen la misma cantidad de letras
if long1 != long2:
    print("No es un anagrama")

else:
    es_anagrama = True

    #recorre letra
    for letra in palabra1:

        conteo1 = 0
        conteo2 = 0

    #contar cuántas veces aparece en palabra 1

    for l in palabra1:
        if l == letra:
            conteo1 += 1

    #veces que aparece en palabra 2
    for l in palabra2:
        if l == letra:
            conteo2 += 1
            
    if conteo1 != conteo2:
        es_anagrama = False

if es_anagrama == True:
    print("Es un anagrama")
else:
    print("No es anagrama")
    

##FUE PROPORCIONADO POR LA IA
"""
def are_anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

print(are_anagrams("Roma", "Amor"))
print(are_anagrams("Amiga", "Magia"))
print(are_anagrams("Jorge", "Jergo"))

#Respuesta de mouredev
