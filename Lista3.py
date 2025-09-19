#Van a crear una lista vacia con su nombre y van a agregar 5 elementos con input: (Nombre, preparatoria, lugar de recidencia, edad, carrera)

#Se crea una lista
Lista_Datos = []

print("Lista de mis datos")
#Agregar dato
Nombre = input(" Ingresa tu nombre: ")
Lista_Datos.append(Nombre)

Preparatoria = input(" Ingresa el nombre de tu preparatoria: ")
Lista_Datos.append(Preparatoria)

LugarDeRecidencia = input(" Ingresa tu lugar de recidencia: ")
Lista_Datos.append(LugarDeRecidencia)

Edad = input(" Ingresa tu edad: ")
Lista_Datos.append(Edad)

Carrera = input(" Ingresa el nombre de tu carrera: ")
Lista_Datos.append(Carrera)

print("\n📌 Tu lista de datos es:")
for Nombre in Lista_Datos:
    print(f"- {Nombre}")

    print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/