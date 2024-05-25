#parte 6 (4)
##ejecutivos.csv. En cada uno de estos archivos los datos se encuentran
#separados por una coma (,) y en cada línea del archivo se encuentra una
#cuenta o un ejecutivo, respectivamente.

#importar cvs


#Vamos a hacer un menú, donde vamos a abrir las tablas donde está la información
#Voy a partir de que ya creamos las "cuenta de crédito", "Cuentas de crédito",
#"cuentas de nomina" "ejecutivos de cuenta"

#Coloco el archivo cuentas.txt, ejecutivos.txt, aperturas.txt
REPORTEC= 'cuentas.txt'
REPORTEE= 'ejecutivos.txt'
REPORTEA= 'aperturas.txt'
#definimos el programa
def banca():
#Colocamos los condicionales para que el usuario interactue con el menu
    preguntar = True
    while preguntar:

        opcion = input("Seleccione una opción:")
        opcion = int(opcion)
print(banca())
#Vamos a agragar los constructores ya creados (colocar en la parte de print)
    elif1 opcion == "1":
        print("1) Cuentas")
        preguntar = False
    elif opcion == "2":
        print("2) Ejecutivos")
        preguntar = False
    elif opcion == "3":
        print("3) Generar reportes")
        preguntar = False
    elif opcion == "4":
        print("4) Salir")
        preguntar = False
    else:
        print("Opción invalida, volver a preguntar :))")
        preguntar = True
#Aquí vamos a colocar los constructores


#Colocar el constructor para abrir los reportes

        # Colocar la parte de agregar cuentas 1
def mostrar_menu():
    print("Seleccione apartado que quiera visitar")
    print("1) Cuentas")
    print("2) Ejecutivos")
    print("3) Generar reportes")
    print("4) Cerrar")
#mandar a llamar solo con su nombre,  las validaciones.
print(mostrar_menu())