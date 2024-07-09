listadenombres = []

def ingresanombre():
    nombre = input("Escribe a continuación un nombre:  ")
    listadenombres.append(nombre)

def devuelvenombres():
    print("Has ingresado todos estos nombres hasta ahora: ")
    print(listadenombres)

def decideusuario():
    while True:
        decision = input("""
        ¿Qué quieres hacer ahora?
        
        1 - Ingresar otro nombre
        2 - Ver la lista de nombres que he ingresado
        3 - Quiero terminar

        """)
        if decision == '1':
            ingresanombre()
            print("Este nombre se agregó a la lista")
        elif decision == "2":
            devuelvenombres()
        elif decision == "3":
            print("Muchas gracias. Aquí finalizamos")
            break
        else:
            print("No seleccionaste una opción válida")

if __name__ == "__main__":
    ingresanombre()  # Inicia con la primera entrada de nombre
    decideusuario()