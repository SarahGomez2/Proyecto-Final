#intento 1 para compilar codigo completo 
import Cuenta as c

class Debito(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_corte, sucursal, estado, correo, telefono):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_cuenta: Número de cuenta del cliente.
        :param float saldo: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_corte: Fecha de corte de la cuenta de débito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        """
        super().__init__(nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_corte, sucursal, estado, correo, telefono)

    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("producto", "cuenta").replace("Monto", "Saldo").replace("acción", "corte"),

    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de débito.
        :return: Representación iterable de una cuenta de débito.
        :rtype: iterable
        """
        return iter(["Débito", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado])


if __name__ == "__main__":
    debito = Debito("Louisa Martínez López", "000002", "1234",
                    60000, "23-02-23", "27-03-23", 2, "Ciudad de México",
                    "loumarp@gmail.com", "5587926947")

    print(debito)

class Credito(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_tarjeta, importe, fecha_apertura,
                 fecha_pago, sucursal, estado, correo, telefono, monto_usado, fecha_vencimiento):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_tarjeta: Numero de tarjeta del cliente.
        :param float importe: Cantidad de dinero del crédito de la tarjeta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_pago: Fecha de pago de la cuenta de crédito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        :param float monto_usado: Monto del crédito usado.
        :param str fecha_vencimiento:
        """
        super().__init__(nombre_cliente, numero_cliente, numero_tarjeta, importe, fecha_apertura,
                         fecha_pago, sucursal, estado, correo, telefono)

        self.__monto_usado = monto_usado

        try:
            self.__fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_vencimiento)

    #GETTERS
    @property
    def monto_usado(self):
        """
        Método para obtener el monto usado del importe del crédito.
        :return: Monto usado del crédito.
        :rtype: float
        """
        return self.__monto_usado

    @property
    def fecha_vencimiento(self):
        """
        Método para obtener la fecha de vencimiento de la tarjeta.
        :return: Fecha de vencimiento de la tarjeta.
        :rtype: datetime.date
        """
        return self.__fecha_vencimiento

    #SETTERS
    @monto_usado.setter
    def monto_usado(self, monto_usado: float):
        """
        Método que permite establecer el monto usado del crédito.
        :param float monto_usado: Monto usado del crédito.
        """
        self.__monto_usado = monto_usado

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento:str):
        """
        Método que permite establecer la fecha de vencimiento de la tarjeta.
        :param fecha_vencimiento: Fecha de vencimiento de la tarjeta.
        """
        try:
            self.__fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_vencimiento)



    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("producto", "tarjeta").replace("Monto", "Importe").replace("acción", "pago") + \
            "Monto usado del crédito: {} \n Fecha de vencimiento de la tarjeta: {}\n".format(self.__monto_usado, self.__fecha_vencimiento)


    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de crédito.
        :return: Representación iterable de una cuenta de crédito.
        :rtype: iterable
        """
        return iter(["Crédito", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado], self.__monto_usado, self.__fecha_vencimiento)


if __name__ == "__main__":
    credito = Credito("Michael Vázquez Esparza", "000003", "12345681",
                    250000, "07-03-23", "10-03-23", 2, "Ciudad de México",
                    "michavaz@gmail.com", "5512164325")

    print(credito)

class Nómina(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_deposito, sucursal, estado, correo, telefono, rfc_empresa, nombre_empresa):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_cuenta: Numero de la cuenta del cliente.
        :param float saldo: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_deposito: Fecha de pago de la cuenta de crédito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        :param str rfc_empresa: RFC de la empresa.
        :param str nombre_empresa: Nombre de la empresa.
        """
        super().__init__(nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                         fecha_deposito, sucursal, estado, correo, telefono)

        self.__rfc_empresa = rfc_empresa
        self.__nombre_empresa = nombre_empresa


    #GETTERS
    @property
    def rfc_empresa(self):
        """
        Método para obtener el RFC de la empresa
        :return: RFC de la empresa.
        :rtype: str
        """
        return self.__rfc_empresa

    @property
    def nombre_empresa(self):
        """
        Método para obtener el nombre de la empresa.
        :return: Nombre de la empresa.
        :rtype: str
        """
        return self.__nombre_empresa

    #SETTERS
    @rfc_empresa.setter
    def rfc_empresa(self, rfc_empresa: str):
        """
        Método que permite establecer el RFC de la empresa.
        :param rfc_empresa: RFC de la empresa.
        """
        self.__rfc_empresa = rfc_empresa

    @nombre_empresa.setter
    def nombre_empresa(self, nombre_empresa:str):
        """
        Método que permite establecer el nombre de la empresa.
        :param nombre_empresa: Nombre de la empresa
        """
        self.__nombre_empresa = nombre_empresa



    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("producto", "cuenta").replace("Monto", "Saldo").replace("acción", "depósito") + \
            "RFC de la empresa: {} \n Nombre de la empresa: {}\n".format(self.__rfc_empresa, self.__nombre_empresa)


    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de nómina.
        :return: Representación iterable de una cuenta de nómina.
        :rtype: iterable
        """
        return iter(["Nómina", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado], self.__rfc_empresa, self.__nombre_empresa)


if __name__ == "__main__":
    nomina = Nomina("Vittorino Bianco ", "000004", "12345694",
                    250000, "07-03-23", "10-03-23", 2, "Ciudad de México",
                    "vittorinocic@gmail.com", "5585471216")

    print(nomina)


from datetime import date
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

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

class Cuenta:
    def __init__(self, nombre_cliente, numero_cliente, numero_producto, monto, fecha_apertura,
                 fecha_accion, sucursal, estado, correo, telefono):
        """
        Constructor de una cuenta base.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_producto: Número del producto contratado por el cliente.
        :param float monto: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_accion: Fecha en la que la cuenta recibe una acción con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        """
        
        self.__nombre_cliente = nombre_cliente
        self.__numero_cliente = numero_cliente
        self.__numero_producto = numero_producto
        self.__monto = monto
        
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha de apertura ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_apertura)
            
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print(("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_accion)

        self.__sucursal = sucursal
        self.__estado = estado

        try:
            self.__correo = validate_email(correo)
        except EmailNotValidError:
            print("El correo ingresado: {} no tiene un formato válido\n").format(correo)

        self.__telefono = telefono


    #GETTERS
    @property
    def nombre_cliente(self):
        """
        Método para obtener el nombre completo del cliente.
        :return: Nombre completo del cliente.
        :rtype: str
        """
        return self.__nombre_cliente

    @property
    def numero_cliente(self):
        """
        Método para obtener el número de cliente.
        :return: Número de cliente.
        :rtype: str
        """
        return self.__numero_cliente

    @property
    def numero_producto(self):
        """
        Método para obtener el número del producto del cliente.
        :return: Número del producto.
        :rtype: str
        """
        return self.__numero_producto

    @property
    def monto(self):
        """
        Método para obtener el monto disponible en la cuenta.
        :return: Monto de dinero en la cuenta.
        :rtype: float
        """
        return self.__monto

    @property
    def fecha_apertura(self):
        """
        Método para obtener la fecha de apertura de la cuenta.
        :return: Fecha de apertura de la cuenta.
        :rtype: datetime.date
        """
        return self.__fecha_apertura

    @property
    def fecha_accion(self):
        """
        Método para obtener la fecha en la que la cuenta recibe una acción.
        :return: Fecha en la que la cuenta recibe una acción.
        :rtype: datetime.date
        """
        return self.__fecha_accion

    @property
    def sucursal(self):
        """
        Método para obtener el número de sucursal.
        :return: Número de sucursal.
        :rtype: int
        """
        return self.__sucursal

    @property
    def estado(self):
        """
        Método para obtener el estado de la República a la que pertenece la sucursal.
        :return: Estado de la República a la que pertenece la sucursal.
        :rtype: str
        """
        return self.__estado

    @property
    def correo(self):
        """
        Método para obtener el correo electrónico del cliente.
        :return: Correo electrónico del cliente.
        :rtype: str
        """
        return self.__correo

    @property
    def telefono(self:str):
        """
        Método para obtener el número de teléfono del cliente.
        :return: Número de telefono del cliente.
        :rtype: str
        """
        return self.__telefono

    #SETTERS
    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente:str):
        """
        Método que permite establecer el nombre del cliente.
        :param nombre_cliente: Nombre del cliente.
        """
        self.__nombre_cliente = nombre_cliente

    @numero_cliente.setter
    def numero_cliente(self, numero_cliente:str):
        """
        Método que permite establecer el número de cliente.
        :param numero_cliente: Número del cliente.
        """
        self.__numero_cliente = numero_cliente

    @numero_producto.setter
    def numero_producto(self, numero_producto:str):
        """
        Método que permite establecer el número del producto contratado por el cliente.
        :param numero_producto: Número del producto contratado por el cliente.
        """
        self.__numero_producto = numero_producto

    @monto.setter
    def monto(self, monto:float):
        """
        Método que permite establecer el monto de dinero en la cuenta.
        :param monto: Monto de dinero en la cuenta.
        """
        self.__monto = monto

    @fecha_apertura.setter
    def fecha_apertura(self, fecha_apertura:str):
        """
        Método que permite establecer la fecha de apertura de la cuenta.
        :param fecha_apertura: Fecha de apertura de la cuenta.
        """
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha de apertura ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_apertura)

    @fecha_accion.setter
    def fecha_accion(self, fecha_accion:str):
        """
        Método que permite establecer la fecha de la accion aplicada a la cuenta.
        :param fecha_accion: Fecha de la accion aplicada a la cuenta.
        """
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n").format(fecha_accion)

    @sucursal.setter
    def sucursal(self, sucursal:int):
        """
        Método que permite establecer el número de sucursal a la que pertenece la cuenta.
        :param sucursal: El número de sucursal.
        """
        self.__sucursal = sucursal

    @estado.setter
    def estado(self, estado:str):
        """
        Método que permite establecer el estado de la República al cual pertenece la sucursal.
        :param estado: Estado de la República al cual pertenece la sucursal.
        """
        self.__estado = estado

    @correo.setter
    def correo(self, correo:str):
        """
        Método que permite establecer el correo electrónico del cliente.
        :param correo: Correo electrónico del cliente.
        """
        try:
            self.__correo = validate_email(correo)
        except EmailNotValidError:
            print("El correo ingresado: {} no tiene un formato válido\n").format(correo)

    @telefono.setter
    def telefono(self, telefono:str):
        """
        Método que permite establecer el número de teléfono del cliente.
        :param telefono: Número de teléfono del cliente.
        """
        self.__telefono = telefono

    #Método STR
    def __str__(self):
        """
        Método para imprimir una cuenta como cadena.
        :return: La cuenta en formato cadena
        :rtype: str
        """
        return "Cuenta:\n Nombre del cliente: {}\n Número de cliente: {}\n Número de producto: {}\n" + \
            "Monto: {}\n Fecha de apertura: {}\n, Fecha de acción: {}\ Sucursal: {}\n" + \
            "Estado: {}\n Correo: {}\n Teléfono: {}".format(self.__nombre_cliente,
                                                            self.__numero_cliente,
                                                            self.__numero_producto,
                                                            self.__monto,
                                                            self.__fecha_apertura.strftime("%d-%m-%Y"),
                                                            self.__fecha_accion.strftime("%d-%m-%Y"),
                                                            self.__sucursal,
                                                            self.__estado,
                                                            self.__correo,
                                                            self.__teléfono)

    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta.
        :return: Representación iterable de una cuenta.
        :rtype: iterable
        """
        return iter(["Cuenta", self.__nombre_cliente, self.__numero_cliente, self.__numero_producto,
                     self.__monto, self.__fecha_apertura, self.__fecha_accion, self.__sucursal,
                     self.__estado, self.__correo, self.__estado])

if __name__ == "__main__":
    cuenta = Cuenta("Luis Francisco Revuelta", "000001", "12345678",
                    100000, "15-04-23", "25-05-23", 4, "Ciudad de México",
                    "luisfrancis@gmail.com", "5534689876")
    print(cuenta)

while True:
   print("1. Crear nueva cuenta")
   print("2. Actualizar datos de la cuenta")
   print("3. Registrar una nueva apertura de cuenta")
   print("4. Dar de alta nuevo empleado")
   print("5. Actualizar datos de un empleado")
   print("[R] Regresar al menu anterior")
    accion = input("¿Qué deseas hacer? ").upper()
     if accion not in "1,2,3,4,5,R" or len(accion) > 2:
      print("No sé qué deseas hacer!\n")
      continue
  else:
      match accion:
    case "1":  # Crear cuenta
     while True:
       print("1. Cuenta de credito")
       print("2. Cuenta de debito")
       print("3. Cuenta de nomina")
        print("[R] Regresar al menu anterior")
       accion = input("¿Qué deseas hacer? ").upper()
       if accion not in "1,2,3,R" or len(accion) > 2:
           print("No sé qué deseas hacer!\n")
           continue
       else:
           match accion:
               case "1": #Crear cuenta de credito
                try:
                  cuenta = #Se genera automaticamente
                  sucursal = while True:
                       print("1. Sucursal CDMX")
                       print("2. Sucursal Cancún")
                       print("3. Sucursal Monterrey")
                       print("4. Sucursal Guadalajara")
                       print("5. Sucursal Oaxaca")
                       print("6. Sucursal Puebla")
                       accion = input("¿Qué sucursal? ").upper()
                       if accion not in "1,2,3,4,5,6" or len(accion) > 2:
                           print("No existe esa opcion\n")
                                  continue
                       else:
                            match accion:
                                case "1": 
                                    sucursal = cdmx
                                case "2":
                                    sucursal = cancun
                                case "3":
                                    sucursal = monterrey
                                case "4":
                                    sucursal = guadalajara
                                case "5":
                                    sucursal = oaxaca
                                case "6":
                                    sucursal = puebla
                  nombre = input("Escriba el nombre del cliente: ")
                  apellidos = input("Escriba los apellidos del cliente: ")
                  apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                  mail = input("Escribe el correo del cliente: ")
                  telefono = input("Escribe el telefono del cliente: ")
                  estado = if sucursal = cdmx: 
                            print "Ciudad de Mexico"
                           elif sucursal = cancun:
                            print "Quintana Roo"
                           elif sucursal = monterrey:
                            print "Nuevo Leon"
                           elif sucursal = guadalajara:
                            print "Jalisco"
                           elif sucursal = oaxaca:
                            print "Oaxaca"
                           elif sucursal = puebla:
                            print "Puebla"
                           else:
                            print "No existe esa opcion\n"
                  vencimiento = input("Escribe la fecha de vencimiento (dd-mm-yyyy): ")
                  credito = input("Escriba el importe de credito: ")
                  utilizado = input("Escriba el monto de credito utilizado: ")
                  pago = input("Escribe la fecha de pago (dd-mm-yyyy): ")
                  # Agregamos al cliente a nuestra lista
                  lista_credito.append(c.Cliente(nombre,
                                                  apellidos,
                                                  datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                  float(salario),
                                                  mail, telefono, estado, float(credito), float(utilizado), cuenta, sucursal, datetime.strptime(vencimiento,                                                   "%d-%m-%Y").date(), datetime.strptime(pago, "%d-%m-%Y").date(),)
                  print("Se agregó el cliente\n")
                except ValueError:
                  print("La fecha no corresponde con el formato dd-mm-yyyy\n")
                
              case "2":  # Crear cuenta de debito
              try:
                cuenta = #Se genera automaticamente
                sucursal = while True:
                    print("1. Sucursal CDMX")
                    print("2. Sucursal Cancún")
                    print("3. Sucursal Monterrey")
                    print("4. Sucursal Guadalajara")
                    print("5. Sucursal Oaxaca")
                    print("6. Sucursal Puebla")
                    accion = input("¿Qué sucursal? ").upper()
                        if accion not in "1,2,3,4,5,6" or len(accion) > 2:
                           print("No existe esa opcion\n")
                                continue
                        else:
                            match accion:
                              case "1": 
                                sucursal = cdmx
                              case "2":
                                sucursal = cancun
                              case "3":
                                sucursal = monterrey
                              case "4":
                                sucursal = guadalajara
                              case "5":
                                sucursal = oaxaca
                              case "6":
                                sucursal = puebla
                nombre = input("Escriba el nombre del cliente: ")
                apellidos = input("Escriba los apellidos del cliente: ")
                apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                mail = input("Escribe el correo del cliente: ")
                telefono = input("Escribe el telefono del cliente: ")
                estado = if sucursal = cdmx: 
                         print "Ciudad de Mexico"
                        elif sucursal = cancun:
                         print "Quintana Roo"
                        elif sucursal = monterrey:
                         print "Nuevo Leon"
                        elif sucursal = guadalajara:
                         print "Jalisco"
                        elif sucursal = oaxaca:
                         print "Oaxaca"
                        elif sucursal = puebla:
                         print "Puebla"
                        else:
                         print "No existe esa opcion\n"
                corte = input("Escribe la fecha de corte (dd-mm-yyyy): ")
                saldo = input("Escriba el saldo inicial: ")
                # Agregamos al cliente a nuestra lista
                lista_debito.append(c.Cliente(nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                      float(salario), mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                      datetime.strptime(corte, "%d-%m-%Y").date(),)
                    print("Se agregó el cliente\n")
                    except ValueError:
                        print("La fecha no corresponde con el formato dd-mm-yyyy\n")
    
              case "3":  # Crear cuenta de nomina
              try:
                cuenta = #Se genera automaticamente
                sucursal = while True:
                    print("1. Sucursal CDMX")
                    print("2. Sucursal Cancún")
                    print("3. Sucursal Monterrey")
                    print("4. Sucursal Guadalajara")
                    print("5. Sucursal Oaxaca")
                    print("6. Sucursal Puebla")
                   accion = input("¿Qué sucursal? ").upper()
                      if accion not in "1,2,3,4,5,6" or len(accion) > 2:
                        print("No existe esa opcion\n")
                          continue
                      else:
                         match accion:
                           case "1": 
                             sucursal = cdmx
                           case "2":
                             sucursal = cancun
                           case "3":
                             sucursal = monterrey
                           case "4":
                             sucursal = guadalajara
                           case "5":
                             sucursal = oaxaca
                           case "6":
                             sucursal = puebla
                nombre = input("Escriba el nombre del cliente: ")
                apellidos = input("Escriba los apellidos del cliente: ")
                apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                mail = input("Escribe el correo del cliente: ")
                telefono = input("Escribe el telefono del cliente: ")
                estado = if sucursal = cdmx: 
                         print "Ciudad de Mexico"
                        elif sucursal = cancun:
                         print "Quintana Roo"
                        elif sucursal = monterrey:
                         print "Nuevo Leon"
                        elif sucursal = guadalajara:
                         print "Jalisco"
                        elif sucursal = oaxaca:
                         print "Oaxaca"
                        elif sucursal = puebla:
                         print "Puebla"
                        else:
                         print "No existe esa opcion\n"
                corte = input("Escribe la fecha de corte (dd-mm-yyyy): ")
                saldo = input("Escriba el saldo inicial: ")
                # Agregamos la persona a nuestra lista
                lista_nomina.append(c.Cliente(nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                float(salario), mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                                datetime.strptime(corte,"%d-%m-%Y").date(),)
                  print("Se agregó el cliente\n")
                  except ValueError:
                  print("La fecha no corresponde con el formato dd-mm-yyyy\n")
                
    
    case "2":  # Actualizar los datos de una cuenta 
    while True:
      print("1. Cuenta de credito")
      print("2. Cuenta de debito")
      print("3. Cuenta de nomina")
           print("[R] Regresar al menu anterior")
           accion = input("¿Qué deseas hacer? ").upper()
           if accion not in "1,2,3,R" or len(accion) > 2:
               print("No sé qué deseas hacer!\n")
               continue
           else:
               match accion:
                   case "1": #Buscar en cuentas de credito
                    try:
                      print ("Ingrese el nombre y el numero de cuenta: ") #Creo que aqui va algo de True, en vez de ese print
                      if not lista_credito:  # Comprueba si la lista está vacía
                        print("La lista de Clientes está vacía!\n")
                      else:  # La lista no está vacía
                        encontro = False  # Indica que aún no la hemos encontrado
                        nombre = input("Escribe el nombre del cliente: ")
                        cuenta = input("Escribe el numero de cuenta: ")
                        # Comenzamos la búsqueda de clintes por nombre y numero de cuenta
                        for cliente in lista_credito:  
                         if (cliente.nombre == nombre and
                             cliente.cuenta == cuenta):
                          print(cliente)  # Encontramos al cliente y lo imprimimos
                        encontro = True  # Indica que ya no necesito seguir buscando
                        print()
                         break  # Rompemos el ciclo for, para ya no buscar
                         if not encontro:  # Si se recorrió la lista y no encontró nada
                         print("El cliente {} con numero de cuenta {} no fue encontrado".format(nombre, cuenta))
                      print ("Los datos actuales de la cuenta son: (nombre,
                                                  apellidos,
                                                  datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                  float(salario),
                                                  mail, telefono, estado, float(credito), float(utilizado), cuenta, sucursal, datetime.strptime(vencimiento,                                                   "%d-%m-%Y").date(), datetime.strptime(pago, "%d-%m-%Y").date(),)")
                      print ("Es el cliente que buscabas?")
                          if true:
                            print ("Estos son los datos que puedes actualizar, modifica solo los necesarios")
                            nombre = input("Escriba el nombre del cliente: ")
                            apellidos = input("Escriba los apellidos del cliente: ")
                            apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                            mail = input("Escribe el correo del cliente: ")
                            telefono = input("Escribe el telefono del cliente: ")
                            estado = if sucursal = cdmx: 
                                      print "Ciudad de Mexico"
                                     elif sucursal = cancun:
                                      print "Quintana Roo"
                                     elif sucursal = monterrey:
                                      print "Nuevo Leon"
                                     elif sucursal = guadalajara:
                                      print "Jalisco"
                                     elif sucursal = oaxaca:
                                      print "Oaxaca"
                                     elif sucursal = puebla:
                                      print "Puebla"
                                     else:
                                       print "No existe esa opcion\n"
                            vencimiento = input("Escribe la fecha de vencimiento (dd-mm-yyyy): ")
                            credito = input("Escriba el importe de credito: ")
                            utilizado = input("Escriba el monto de credito utilizado: ")
                            pago = input("Escribe la fecha de pago (dd-mm-yyyy): ")
                            # Actualizamos los datos del cliente en nuestra lista
                              lista_credito.append(c.Cliente(nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                            float(salario), mail, telefono, estado, float(credito), float(utilizado), 
                                                            cuenta,sucursal, datetime.strptime(vencimiento,"%d-%m-%Y").date(), 
                                                             datetime.strptime(pago, "%d-%m-%Y").date(),)
                              print("Se actualizaron los datos!\n")
                            except ValueError:
                              print("La fecha no corresponde con el formato dd-mm-yyyy\n")
                          else:
                            print ("Intentelo de nuevo")
                              #Que lo regrese al menu anterior
    
                    case "2": #Buscar en cuentas de debito
                    try:
                       print ("Ingrese el nombre y el numero de cuenta: ") #Creo que aqui va algo de True, en vez de ese print
                       if not lista_debito:  # Comprueba si la lista está vacía
                         print("La lista de Clientes está vacía!\n")
                       else:  # La lista no está vacía
                         encontro = False  # Indica que aún no la hemos encontrado
                         nombre = input("Escribe el nombre del cliente: ")
                         cuenta = input("Escribe el numero de cuenta: ")
                        # Comenzamos la búsqueda de clientes por nombre y numero de cuenta
                        for cliente in lista_debito:  
                        if (cliente.nombre == nombre and
                            cliente.cuenta == cuenta):
                         print(cliente)  # Encontramos al cliente y lo imprimimos
                         encontro = True  # Indica que ya no necesito seguir buscando
                         print()
                        break  # Rompemos el ciclo for, para ya no buscar
                           if not encontro:  # Si se recorrió la lista y no encontró nada
                          print("El cliente {} con numero de cuenta {} no fue encontrado".format(nombre, cuenta))
                      print ("Los datos actuales de la cuenta son: (nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                   float(salario), mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                   datetime.strptime(corte, "%d-%m-%Y").date(),))
                    print ("Es el cliente que buscabas?")
                        if true:
                          print ("Estos son los datos que puedes actualizar, modifica solo los necesarios")
                            nombre = input("Escriba el nombre del cliente: ")
                            apellidos = input("Escriba los apellidos del cliente: ")
                            apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                            mail = input("Escribe el correo del cliente: ")
                            telefono = input("Escribe el telefono del cliente: ")
                            estado = if sucursal = cdmx: 
                                      print "Ciudad de Mexico"
                                     elif sucursal = cancun:
                                      print "Quintana Roo"
                                     elif sucursal = monterrey:
                                      print "Nuevo Leon"
                                     elif sucursal = guadalajara:
                                      print "Jalisco"
                                     elif sucursal = oaxaca:
                                      print "Oaxaca"
                                     elif sucursal = puebla:
                                      print "Puebla"
                                     else:
                                      print "No existe esa opcion\n"
                            corte = input("Escribe la fecha de corte (dd-mm-yyyy): ")
                            saldo = input("Escriba el saldo inicial: ")
                                  # Agregamos al cliente a nuestra lista
                            lista_debito.append(c.Cliente(nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                          mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                                          datetime.strptime(corte, "%d-%m-%Y").date(),)
                            print("Se actualizaron los datos!\n")
                            except ValueError:
                             print("La fecha no corresponde con el formato dd-mm-yyyy\n")
                        else:
                          print ("Intentelo de nuevo")
                          #Que lo regrese al menu anterior
                                                
                    case "3": #Buscar en cuentas de nomina
                    try:
                        print ("Ingrese el nombre y el numero de cuenta: ") #Creo que aqui va algo de True, en vez de ese print
                        if not lista_nomina:  # Comprueba si la lista está vacía
                         print("La lista de Personas está vacía!\n")
                        else:  # La lista no está vacía
                        encontro = False  # Indica que aún no la hemos encontrado
                        nombre = input("Escribe el nombre del cliente: ")
                        cuenta = input("Escribe el numero de cuenta: ")
                         # Comenzamos la búsqueda de clientes por nombre y numero de cuenta
                        for cliente in lista_nomina:  
                         if (cliente.nombre == nombre and
                             cliente.cuenta == cuenta):
                         print(cliente)  # Encontramos al cliente y lo imprimimos
                         encontro = True  # Indica que ya no necesito seguir buscando
                         print()
                         break  # Rompemos el ciclo for, para ya no buscar
                          if not encontro:  # Si se recorrió la lista y no encontró nada
                        print("El cliente {} con numero de cuenta {} no fue encontrado".format(nombre, cuenta))
                         print ("Los datos actuales de la cuenta son: (nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                    float(salario), mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                    datetime.strptime(corte,"%d-%m-%Y").date(),)
                        print ("Es el cliente que buscabas?")
                           if true:
                             print ("Estos son los datos que puedes actualizar, modifica solo los necesarios")
                                nombre = input("Escriba el nombre del cliente: ")
                                apellidos = input("Escriba los apellidos del cliente: ")
                                apertura = input("Escribe la fecha de apertura (dd-mm-yyyy): ")
                                mail = input("Escribe el correo del cliente: ")
                                telefono = input("Escribe el telefono del cliente: ")
                                estado = if sucursal = cdmx: 
                                         print "Ciudad de Mexico"
                                        elif sucursal = cancun:
                                         print "Quintana Roo"
                                        elif sucursal = monterrey:
                                         print "Nuevo Leon"
                                        elif sucursal = guadalajara:
                                         print "Jalisco"
                                        elif sucursal = oaxaca:
                                         print "Oaxaca"
                                        elif sucursal = puebla:
                                         print "Puebla"
                                        else:
                                         print "No existe esa opcion\n"
                                corte = input("Escribe la fecha de corte (dd-mm-yyyy): ")
                                saldo = input("Escriba el saldo inicial: ")
                                # Agregamos la persona a nuestra lista
                                lista_nomina.append(c.Cliente(nombre, apellidos, datetime.strptime(apertura, "%d-%m-%Y").date(),
                                                                                float(salario), mail, telefono, estado, float(saldo), cuenta, sucursal, 
                                                                                datetime.strptime(corte,"%d-%m-%Y").date(),)
                                print("Se actualizaron los datos!\n")
                                except ValueError:
                                print("La fecha no corresponde con el formato dd-mm-yyyy\n")
                           else:
                            print ("Intentelo de nuevo")
                            #Que lo regrese al menu anterior
                                                    
    case "3":  # Registrar una nueva apertura de cuenta
    try:
    #Debo anadir las cuentas registradas en el dia en un solo documento, que tanga los datos de la cuenta y del empleado que la ingreso
                      
    case "4": #Dar de alta un empleado
    try:
       cuenta = #Se genera automaticamente
       nombre = input("Escriba el nombre del empleado: ")
       apellidos = input("Escriba los apellidos del empleado: ")
       mail = input("Escribe el correo del empleado: ")
       telefono = input("Escribe el telefono del empleado: ")
       salario = input("Escribe el salario mensual del empleado: ")
       direccion = input("Escribe la direccion del empleado: ")    
       rfc = input("Escriba el RFC del empleado: ")                         
       lista_empleados.append(e.Empleado(nombre, apellidos, telefono, direccion, rfc,
                                       float(salario), mail))
       print("Se agregó al empleado a la lista\n")
       except ValueError:
       print("La fecha no corresponde con el formato dd-mm-yyyy\n")

    case "5": #Actualizar datos de un empleado
    try: 
      print ("Ingrese el nombre y los apellidos: ")
      if not lista_empleados:  # Comprueba si la lista está vacía
       print("La lista de Empleados está vacía!\n")
      else:  # La lista no está vacía
       encontro = False  # Indica que aún no la hemos encontrado
       nombre = input("Escribe el nombre del empleado: ")
       apellidos = input("Escribe los apellidos del empleado: ")
      # Comenzamos la búsqueda de empleados por nombre y apellidos
      for empleados in lista_empleados:  # Cada persona en la lista se asocia con per
       if (empleado.nombre == nombre and
           empleado.apellidos == apellidos):
       print(empleado)  # Encontramos al empleado y la imprimimos
        encontro = True  # Indica que ya no necesito seguir buscando
       print()
       break  # Rompemos el ciclo for, para ya no buscar
        if not encontro:  # Si se recorrió la lista y no encontró nada
      print("El empleado {} {} no fue encontrada".format(nombre, apellidos))
      print ("Los datos actuales del empleado son: (e.Empleado(nombre, apellidos, telefono, direccion, rfc,
                                                   float(salario), mail))
      print ("Es el empleado que buscabas?")
      if true:
       print ("Estos son los datos que puedes actualizar, modifica solo los necesarios")
         nombre = input("Escriba el nombre del empleado: ")
         apellidos = input("Escriba los apellidos del empleado: ")
         mail = input("Escribe el correo del empleado: ")
         telefono = input("Escribe el telefono del empleado: ")
         salario = input("Escribe el salario mensual del empleado: ")
         direccion = input("Escribe la direccion del empleado: ")    
         rfc = input("Escriba el RFC del empleado: ")                         
         lista_empleados.append(e.Empleado(nombre, apellidos, telefono, direccion, rfc,
                                float(salario), mail))
        print("Se actualizaron los datos!\n")
        except ValueError:
        print("La fecha no corresponde con el formato dd-mm-yyyy\n")
      else:
       print ("Intentelo de nuevo")
       #Que lo regrese al menu anterior
                                                    
    case "R":
            

#Armamos el menú
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




