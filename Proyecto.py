from tabla_periodica import elementos
import random
grupos = {
     "1": ["1", "metales alcalinos", "grupo 1"],
    "2": ["2", "metales alcalinotérreos", "grupo 2"],
    "3": ["3", "escandio y el grupo del itrio", "escandio", "grupo del itrio", "itrio", "grupo 3"],
    "4": ["4", "grupo del titanio", "titanio", "grupo 4"],
    "5": ["5", "grupo del vanadio", "vanadio", "grupo 5"],
    "6": ["6", "grupo del cromo", "cromo", "grupo 6"],
    "7": ["7", "grupo del manganeso", "manganeso", "grupo 7"],
    "8": ["8", "grupo del hierro", "hierro", "grupo 8"],
    "9": ["9", "grupo del cobalto", "cobalto", "grupo 9"],
    "10": ["10", "grupo del níquel", "níquel", "grupo 10"],
    "11": ["11", "metales de acuñación", "cobre", "plata", "oro", "grupo 11"],
    "12": ["12", "grupo del zinc", "zinc", "grupo 12"],
    "13": ["13", "térreos", "grupo del boro", "boro", "grupo 13"],
    "14": ["14", "carbonoides", "grupo del carbono", "carbono", "grupo 14"],
    "15": ["15", "nitrogenoides", "grupo del nitrógeno", "nitrógeno", "grupo 15"],
    "16": ["16", "calcógenos", "grupo del oxígeno", "oxígeno", "grupo 16"],
    "17": ["17", "halógenos", "grupo 17"],
    "18": ["18", "gases nobles", "grupo 18"]
}
grupo_encontrado = None
def quitar_tildes(texto):
          texto = texto.lower()
          texto = texto.replace("á", "a")
          texto = texto.replace("é", "e")
          texto = texto.replace("í", "i")
          texto = texto.replace("ó", "o")
          texto = texto.replace("ú", "u")
          return texto

def codigo():
    try:
        print ("Quiere poner un elemento, una caracteristica o un quiz? ")
        print ("[1] Característica")
        print ("[2] Elemento")
        print ("[3] Quiz")
        elemento = "no es un elemento"
        primera_elec = input("\nelige una opcion numerica:")
        if primera_elec == "1":
            print ("opciones de la caracteristica:")
            print ("[1] ¿Es radioactivo?")
            print ("[2] Masa Atómica")
            print ("[3] El grupo")
            print ("[4] El periodo")
            print ("[5] El bloque")
            print ("[6] El Numero Atómico")
            simbolo = int(input("\nelige una opcion numerica:"))

            match simbolo:
                case 1: 
                    respuesta = input("¿Es radioactivo?(poner si or no) ")
                    if respuesta == "si":
                        for simbolo, datos in elementos.items():
                            if datos["Radiactivo"] == True:
                                print(f"{datos['Nombre']} cumple la condición")
                    elif respuesta == "no":
                        for simbolo, datos in elementos.items():
                            if datos["Radiactivo"] == False:
                                print(f"{datos['Nombre']} cumple la condición")        
                case 2:
                    print ("/nNivel de masa atómica")
                    print ("[1] Masas bajas (1-20 u)")
                    print ("[2] Masas intermedias (21-100)")
                    print ("[3] Masas altas (101-200)")
                    print ("[4] Masas muy altas (>200)")
                    respuesta = int(input("\nelige una opcion numerica:"))
                    match respuesta:
                        case 1:
                            for simbolo, datos in elementos.items():
                                if datos["MasaAtomica"] > 1 and datos["MasaAtomica"] < 20:
                                    lista_uno = [{datos['Nombre']}]
                                    print( f"{datos['Nombre']} cumple la condición")
                        case 2:
                            for simbolo, datos in elementos.items():
                                if datos["MasaAtomica"] > 21 and datos["MasaAtomica"] < 100:
                                    lista_uno = [{datos['Nombre']}]
                                    print( f"{datos['Nombre']} cumple la condición")
                        case 3:
                            for simbolo, datos in elementos.items():
                                if datos["MasaAtomica"] > 101 and datos["MasaAtomica"] < 200:
                                    lista_uno = [{datos['Nombre']}]
                                    print( f"{datos['Nombre']} cumple la condición")
                        case 4:
                            for simbolo, datos in elementos.items():
                                if datos["MasaAtomica"] > 200:
                                    lista_uno = [{datos['Nombre']}]
                                    print( f"{datos['Nombre']} cumple la condición")
                                 
                case 3:
                    respuesta = input("Pon el nombre del grupo o el número del grupo:").lower()
                    # Buscar a qué grupo pertenece la respuesta
                    for clave, opciones in grupos.items():
                        if respuesta in opciones:
                            grupo_encontrado = int(clave)

                    if grupo_encontrado:
                        for simbolo, datos in elementos.items():
                            if datos["Grupo"] == grupo_encontrado:
                                print(f"{datos['Nombre']} está en el grupo {grupo_encontrado}")
                    else:
                        print("No se reconoció el grupo ingresado.")
                case 4:
                    respuesta = int(input("Pon el número del periodo del elemento: "))
                    for simbolo, datos in elementos.items():
                        if datos["Periodo"] == respuesta:
                            lista_uno = [{datos['Nombre']}]
                            print( f"{datos['Nombre']} cumple la condición")  
                case 5:
                    respuesta = input("Pon el bloque del elemento: ")
                    for simbolo, datos in elementos.items():
                     if datos["Bloque"] == respuesta:
                       lista_uno = [{datos['Nombre']}]
                       print( f"{datos['Nombre']} cumple la condición")
                case 6: 
                    respuesta = int(input("Pon el numero atómico del elemento:"))
                    for simbolo, datos in elementos.items():
                        if datos["NumeroAtomico"] == respuesta:
                            lista_uno = [{datos['Nombre']}]
                            print( f"{datos['Nombre']} cumple la condición")
        elif primera_elec == "2": 
            elemento = input("\nIngrese el nombre de un elemento: ")
            elemento = quitar_tildes(elemento.capitalize())

            if elemento in elementos:
                datos = elementos[elemento]
                for clave, valor in datos.items():   
                    print(f"{clave}: {valor}") # Imprimir en filas
            else:
                print("Elemento no fue encontrado")
        elif primera_elec == "3":
            import Quiz
            print (Quiz)
        else:
            print ("Esa no es una opción")
            codigo()
    except ValueError:
        print ("Hubo un error, empezemos de nuevo :D")
        return codigo ()

score = 0
def quiz():
    try:
        elemento_al_azar= random.choice(list(elementos.keys()))
        global score
        print("¡Empecemos con el quiz! Se eligirá un elemento random y se le tendrá que escribir sus caracteristicas, por cada respuesta bien recibirá un punto y por cada erronea se le restara un punto a ese puntaje."
        "\nEscribe las características de este elemento:", elemento_al_azar)
        primera_pregunta = input("Numero Atómico: ")
        segunda_pregunta = input("Simbolo: ")
        tercera_pregunta = input("Masa Atomica: ")
        cuarta_pregunta = input("Grupo: ")
        quinta_pregunta = input("Periodo: ")
        sexta_pregunta = input("Bloque: ")
        septima_pregunta = input("Radiactividad: ")

        datos = elementos[elemento_al_azar]
        if primera_pregunta.lower() == str(datos["NumeroAtomico"]).strip():
            print("\nNúmero Atómico: Correcto!")
            score +=1
        else:
            print("Número Atómico: Incorrecto")
            score -=1
        if segunda_pregunta.lower() == str(datos["Simbolo"]).strip().lower():
            print("Simbolo: Correcto!")
            score +=1
        else:
            print("Simbolo: Incorrecto")
            score -=1
        if tercera_pregunta.lower() == str(datos["MasaAtomica"]).strip().lower():
            print("Masa atomica: Correcto!")
            score +=1
        else:
            print("Masa atomica: Incorrecto")
            score -=1
        if cuarta_pregunta.lower() == str(datos["Grupo"]).strip().lower():
            print("Grupo: Correcto!")
            score +=1
        else:
            print("Grupo: Incorrecto")
            score -=1
        if quinta_pregunta.lower() == str(datos["Periodo"]).strip().lower():
            print("Periodo: Correcto!")
            score +=1
        else:
            print("Periodo: Incorrecto")
            score -=1
        if sexta_pregunta.lower() == str(datos["Bloque"]).strip().lower():
            print("Bloque: Correcto!")
            score +=1
        else:
            print("Bloque: Incorrecto")
            score -=1
        respuesta_si_no = septima_pregunta.strip().lower()
        es_radiactivo = datos["Radiactivo"]
        if (respuesta_si_no == "si" and es_radiactivo) or (respuesta_si_no == "no" and not es_radiactivo):
            print("Radioactividad: Correcta!")
            score +=1
        else:
            septima_pregunta = False
            print("Radioactividad: Incorrecta")
            score -=1
        print (score)
        respuesta_f = input("\nQuiere jugar de nuevo? (si/no): ").lower().strip()
        if respuesta_f == "si":
            quiz()
        if respuesta_f == "no":
            print("ok!")
    except ValueError:
        ("Parece que hubo un error en el codigo, porque no lo intentas de nuevo ;)")
        codigo()
codigo()