# Programa: listaPersonas.py
# Objetivo: Programa que permite controlar un conjunto de personas
#           a través de una lista, para ver sus operaciones más comunes.
# Author: Gerardo Avilés
# Fecha: 19/04/2024

import Persona as p
from datetime import datetime
import csv  # Lectura/escritura de archivos
from locale import currency
from locale import setlocale
from locale import LC_MONETARY


def __nombremes(mes:int):
    """
    Función privada que devuelve el nombre del mes.
    :param mes: El número de mes válido.
    :return: El nombre del mes.
    :rtype: str
    """
    match mes:
        case 1: nombre = "Enero"
        case 2: nombre = "Febrero"
        case 3: nombre = "Marzo"
        case 4: nombre = "Abril"
        case 5: nombre = "Mayo"
        case 6: nombre = "Junio"
        case 7: nombre = "Julio"
        case 8: nombre = "Agosto"
        case 9: nombre = "Septiembre"
        case 10: nombre = "Octubre"
        case 11: nombre = "Noviembre"
        case 12: nombre = "Diciembre"
    return nombre

# Crear una lista vacía
lista_personas = []
while True:
    print("1. Agregar una persona")
    print("2. Mostrar una persona por nombre y apellido")
    print("3. Eliminar una persona por nombre y apellido")
    print("4. Mostrar todas las personas")
    print("5. Mostrar todas las personas dada una edad")
    print("6. Eliminar todas las personas dada una edad")
    print("7. Leer Personas desde archivo")
    print("8. Guardar Personas en archivo")
    print("9. Mostrar persona por rango de salario")
    print("10. Mostrar persona por mes y año")
    print("[S]alir")
    accion = input("¿Qué deseas hacer? ").upper()
    if accion not in "1,2,3,4,5,6,7,8,9,10,S" or len(accion) > 2:
        print("No sé qué deseas hacer!\n")
        continue
    else:
        match accion:
            case "1":  # Agregar persona
                try:
                    nombre = input("Escribe el nombre de la persona: ")
                    apellidos = input("Escribe los apellidos de la persona: ")
                    nacimiento = input("Escribe la fecha de nacimiento (dd-mm-yyyy): ")
                    salario = input("Escribe el salario de la persona: ")
                    mail = input("Escribe el correo de la persona: ")
                    # Agregamos la persona a nuestra lista
                    lista_personas.append(p.Persona(nombre,
                                                    apellidos,
                                                    datetime.strptime(nacimiento, "%d-%m-%Y").date(),
                                                    float(salario),
                                                    mail))
                    print("Se agregó la persona indicada\n")
                except ValueError:
                    print("La fecha no corresponde con el formato dd-mm-yyyy\n")
            case "2":  # Mostrar una persona por nombre y apellido
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Indica que aún no la hemos encontrado
                    nombre = input("Escribe el nombre de la persona: ")
                    apellidos = input("Escribe los apellidos de la persona: ")
                    # Comenzamos la búsqueda de personas por nombre y apellidos
                    for persona in lista_personas:  # Cada persona en la lista se asocia con per
                        if (persona.nombre == nombre and
                                persona.apellidos == apellidos):
                            print(persona)  # Encontramos a la persona y la imprimimos
                            encontro = True  # Indica que ya no necesito seguir buscando
                            print()
                            break  # Rompemos el ciclo for, para ya no buscar
                    if not encontro:  # Si se recorrió la lista y no encontró nada
                        print("La persona {} {} no fue encontrada".format(nombre, apellidos))
            case "3":  # Eliminar persona por nombre y apellido
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Indica que aún no la hemos encontrado
                    nombre = input("Escribe el nombre de la persona: ")
                    apellidos = input("Escribe los apellidos de la persona: ")
                    # Comenzamos la búsqueda de personas por nombre y apellidos
                    for persona in lista_personas:  # Cada persona en la lista se asocia con per
                        if (persona.nombre == nombre and
                                persona.apellidos == apellidos):
                            lista_personas.remove(persona)  # Encontramos a la persona y la borramos
                            encontro = True  # Indica que ya no necesito seguir buscando
                            break  # Rompemos el ciclo for, para ya no buscar
                    if not encontro:  # Si se recorrió la lista y no encontró nada
                        print("La persona {} {} no fue eliminada".format(nombre, apellidos))
            case "4":  # Imprimir todas las personas
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    for persona in lista_personas:
                        print(persona)  # Imprime las personas una a una
                    print()
            case "5":  # Mostrar todas las personas dada una edad
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Aún no se ha encontrado la persona
                    edad = int(input("Escribe la edad de la persona a buscar: "))
                    # Comenzamos la búsqueda en la lista
                    for persona in lista_personas:  # Recorremos la lista
                        if persona.edad() == edad:
                            encontro = True  # Si encotramos al menos una, la mostramos
                            print(persona)
                    print()
                            # break  # Este break serviría, si solo quisiera una persona
                    if not encontro:  # La persona con la edad indicada, no estaba
                        print("No existen personas de {} años\n".format(edad))
            case "6":  # Eliminar todas las personas dada una edad
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Aún no se ha encontrado la persona
                    edad = int(input("Escribe la edad de la persona a buscar: "))
                    # Comenzamos la búsqueda en la lista
                    for persona in lista_personas:  # Recorremos la lista
                        if persona.edad() == edad:
                            encontro = True  # Si encotramos al menos una, la mostramos
                            lista_personas.remove(persona)
                            # break  # Este break serviría, si solo quisiera una persona
                    if not encontro:  # La persona con la edad indicada, no estaba
                        print("No existen personas de {} años".format(edad))

            case "S":  # Salir
                print("Hasta luego!")
                break

            case "7":  # Leer archivo
                archivo = input("Escribe el  nombre del archivo CSV: ")
                existe = False  # Indica si el archivo se encontró o no
                while not existe:  # Mientras el archivo exista
                    # Abrir el archivo CSV
                    try:
                        with open(archivo, encoding="UTF8", newline="") as file:
                            lector = csv.reader(file)
                            # Dado que hay header, vamos a saltar esa línea
                            lector.__next__()
                            if lista_personas:
                                print("La lista de personas no está vacía")
                                resp = input("¿Deseas agregar otras personas?(y/n): ")
                                if resp.lower()[0] == "n":
                                    lista_personas = []  # Vaciamos la lista
                            for fila in lector:
                                lista_personas.append(p.Persona(fila[0],  # Nombre
                                                                fila[1],  # Apellidos
                                                                datetime.strptime(fila[2], "%Y-%m-%d").date(),  # Nacimiento
                                                                float(fila[3]),  # Salario
                                                                fila[4]))  # Correo
                            existe = True  # Si llegó aquí, el archivo existe
                            print("El archivo de Personas se leyó correctamente\n")
                    except FileNotFoundError:
                        print("El archivo no existe!\n")
                        archivo = input("Escribe el nombre del archivo CSV: ")

            case "8":  # Guardar archivo de Personas
                archivo = input("Escribe el nombre del archivo a guardar: ")
                with open(archivo, "w", encoding="UTF8", newline="") as file:
                    # Utilizando CSV
                    header = ["nombre", "apellidos", "nacimiento", "salario", "mail"]
                    writer = csv.writer(file)
                    # Escribir el encabezado del archivo
                    writer.writerow(header)
                    # Escribir múltiples líneas
                    writer.writerows(lista_personas)
                    print("El archivo {} se guardó con éxito!\n".format(archivo))

            case "9":  # Mostrar todas las personas que tienen un salario en un rango
                setlocale(LC_MONETARY, "en_US")
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Aún no se ha encontrado la persona
                    salario1 = float(input("Escribe el salario inicial: "))
                    salario2 = float(input("Escribe el salario final: "))
                    while salario2 < salario1:
                        print("El segundo final debe ser mayor al inicial!")
                        salario2 = float(input("Escribe el salario final: "))
                    # Comenzamos la búsqueda en la lista
                    for persona in lista_personas:  # Recorremos la lista
                        if salario1 <= persona.salario <= salario2:
                            encontro = True  # Si encotramos al menos una, la mostramos
                            print(persona)
                    print()
                    # break  # Este break serviría, si solo quisiera una persona
                    if not encontro:  # La persona con la edad indicada, no estaba
                        print("No existen personas con salario entre "
                              "{} y {}\n".format(currency(salario1, grouping=True),
                                                 currency(salario2, grouping=True)))

            case "10":  # Mostrar todas las personas que nacieron en un mes y año particular
                if not lista_personas:  # Comprueba si la lista está vacía
                    print("La lista de Personas está vacía!\n")
                else:  # La lista no está vacía
                    encontro = False  # Aún no se ha encontrado la persona
                    mes = input("Escribe el mes a buscar: ")
                    while mes not in "1,2,3,4,5,6,7,8,9,10,11,12":
                        print("El mes debe ser un valor entre 1 y 12!")
                        mes = input("Escribe el mes a buscar: ")
                    año = int(input("Escribe el año a buscar: "))
                    while 0 > año > 9999:
                        print("El año debe estar entre 1 y 9999")
                        año = int(input("Escribe el año a buscar: "))
                    # Comenzamos la búsqueda en la lista
                    for persona in lista_personas:  # Recorremos la lista
                        if persona.nacimiento.year == año and \
                                persona.nacimiento.month == int(mes):
                            encontro = True  # Si encotramos al menos una, la mostramos
                            print(persona)
                    print()
                    # break  # Este break serviría, si solo quisiera una persona
                    if not encontro:  # La persona con la edad indicada, no estaba
                        print("No existen personas que hayan nacido en "
                              "{} del año {}\n".format(__nombremes(int(mes)), año))