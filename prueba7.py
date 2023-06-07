#contador de vocales
def contar_vocales(palabra): 
    vocales = ["a", "e", "i", "o", "u"]
    contador=0
    for letra in palabra:
        if letra.lower() in vocales:
            contador+=1

    return contador


palabra = input("Ingresa una palabra: ")


numero_vocales = contar_vocales(palabra)

print("Número de vocales:", numero_vocales)