print("""
¡Hola!

Bienvenido a TU ELEVADOR
""")

# 1. Definir una lista de pisos

floorlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
firstfloor = floorlist[0]
lastfloor = floorlist[-1]
# 2. Definir el piso actual. 

currentfloor = 1
print("Actualmente estás en el PISO ", str(currentfloor))

# 3. Preguntarle al usuario a qué piso quiere ir.

print("""
    ¿A qué piso te gustaría ir?
""")
for floor in floorlist:
    print(floor)
print(""" """)
destinationfloor = int(input("Ahora escoge el piso: "))
print(""" 
Has escogido el PISO """, str(destinationfloor), """
""")

# 4. Calcular si el ascensor debe subir, bajar, quedarse quieto o terminar el programa
# 5. Realizar la acción de subir o bajar y reflejarlo en el contador de pisos (cada piso)

if destinationfloor <= lastfloor and destinationfloor >= firstfloor and destinationfloor > currentfloor:
    print ("TU ELEVADOR está subiendo")
    while destinationfloor > currentfloor:
        currentfloor = currentfloor + 1      
        print ("PISO " + str(currentfloor))        
elif destinationfloor <= lastfloor and destinationfloor >= firstfloor and destinationfloor < currentfloor:
    print ("TU ELEVADOR está bajando")
    while destinationfloor < currentfloor:
        currentfloor = currentfloor - 1
        print ("PISO " + str(currentfloor))                 
elif destinationfloor == currentfloor:
    print("¡Estás justamente en ese piso!")    
elif destinationfloor < firstfloor or destinationfloor > lastfloor:
    print("Ese piso no existe")
else:
    print("No has seleccionado una opción válida. Gracias por usar TU ELEVADOR.")

# 6. Redefinir el piso actual

print ("""
Ahora estás en el PISO """, str(currentfloor), """
""")


# 7. Volver al paso 3.

