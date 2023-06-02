maya_diccionario = {"rojo": "chak", "naranja": "chak'k'an", "amarillo": "k'an", "verde": "ya'ax",\
"azul": "ch'oj", "violeta": "chakch'oj"}

frances_diccionario = {"rojo": "roux", "naranja": "orange", "amarillo": "jaune", "verde": "vert",\
"azul": "bleu", "violeta": "violette"}

colores = ["rojo", "naranja", "amarillo", "verde", "azul", "violeta"]

#indicar al usuario cuales son los dos idiomas que puedes traducir
 
print("!Hola¡  En este programa prodremos taducir los colores del arcoiris del español en 2 idiomas Frances o Maya")

print("Por favor indica a que color del arcoiris quieres traducir")

while color in colores:

    color = input("Por favor indica un color del arcoiris (rojo, naranja, amarillo, verde, azul o violeta): ")

    print("Por favor indica a que idioma quieres traducir")

    idioma = input("Para traducir en Maya por favor escribe maya y para traducir en frances escribe frances: ")

    while idioma == "maya" or "frances":

            if idioma == "maya":

                frase = input('Escribe un color del arcoiris: ')

                palabras = frase.split()

                respuesta = ' ' #Cadena vacia

                for palabra in palabras:
                    if palabra in maya_diccionario:
                        respuesta = respuesta + maya_diccionario[palabra] + ' '
                    else:
                        respuesta = respuesta + palabra + ' '

                    print(respuesta)

            elif idioma == "fances":

                frase = input('Escribe un color del arcoiris: ')

                palabras = frase.split()

                respuesta = ' ' #Cadena vacia

                for palabra in palabras:
                    if palabra in frances_diccionario:
                        respuesta = respuesta + frances_diccionario[palabra] + ' '
                    else:
                        respuesta = respuesta + palabra + ' '

                    print(respuesta)

            else: 
                print("Por favor elije unicamente frances o maya: ")
                break
        
else:
    print("Ese color no esta en el acoiris")
   

