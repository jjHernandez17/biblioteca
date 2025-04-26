libros = {}
wile1 = True

print("---"*30)
print("BIBLIOTECA")
print("---"*30)
while wile1:
    nombre = input("Agregue un libro al sistema: ")
    id = int(input("Indique el id del libro: "))
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro:  ")
    año = int(input("Ingrese el año de publicacion del libro: "))

    libros[nombre] = id, titulo, autor, año
    print(libros)
    wile2 = True
    while wile2:
        otro = input ("Desea agregar otro libro : (si/no)")
        if otro == "no":
            wile1 = False
            wile2 = False
        elif otro == "si":
            wile2 = False
        else: 
            print("opcion no valida")