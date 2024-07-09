listadenombres = [0]
nombre = input("Escribe a continuación un nombre:  ")
decision = 0
listadenombres.append(nombre)
listadenombres.pop(0)


def ingresanombre():
    nombre = input("Escribe a continuación un nombre:  ")
    listadenombres.append(nombre)
    return


def devuelvenombres():
    print("Has ingresado todos estos nombres hasta ahora: ")
    print(listadenombres)


def decideusuario():
    decision = input("""
   
    ¿Qué quieres hacer ahora?
    
    1 - Ingresar otro nombre
    2 - Ver la lista de nombres que he ingresado
    3 - Quiero terminar

    """)
    if decision == '1':
        nombre = input("Entonces escribe otro nombre:  ")
        listadenombres.append(nombre)
        print(" ")
        print("Este nombre se agregó a la lista")        
        decideusuario()
    elif decision == "2":
        devuelvenombres()
        decideusuario()
    elif decision == "3":
        print("Muchas gracias. Aquí finalizamos")
    else:
        print("No seleccionaste una opción válida")
        decideusuario()
    return


decideusuario()