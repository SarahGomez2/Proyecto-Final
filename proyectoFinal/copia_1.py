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




