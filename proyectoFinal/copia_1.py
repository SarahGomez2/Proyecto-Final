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




