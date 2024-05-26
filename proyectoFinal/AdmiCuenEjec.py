from datetime import date
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Cuenta:
    def _init_(self, nombre_cliente, numero_cliente, numero_producto, monto, fecha_apertura,
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
            print("La fecha de apertura ingresada: {} no está en el formato dd-mm-yyyy\n".format(fecha_apertura))
            
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: {} no está en el formato dd-mm-yyyy\n".format(fecha_accion))

        self.__sucursal = sucursal
        self.__estado = estado

        try:
            self.__correo = validate_email(correo).email
        except EmailNotValidError:
            print("El correo ingresado: {} no tiene un formato válido\n".format(correo))

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
            print("La fecha de apertura ingresada: '{}' no está en el formato dd-mm-yyyy\n".format(fecha_apertura))
####################

    @fecha_accion.setter
    def fecha_accion(self, fecha_accion:str):
        """
        Método que permite establecer la fecha de la accion aplicada a la cuenta.
        :param fecha_accion: Fecha de la accion aplicada a la cuenta.
        """
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n".format(self.__fecha_accion))

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
            print("El correo ingresado: {} no tiene un formato válido\n".format(self.__correo))

    @telefono.setter
    def telefono(self, telefono:str):
        """
        Método que permite establecer el número de teléfono del cliente.
        :param telefono: Número de teléfono del cliente.
        """
        self.__telefono = telefono

    #Método STR
    def _str_(self):
        """
        Método para imprimir una cuenta como cadena.
        :return: La cuenta en formato cadena
        :rtype: str
        """
        return "|CUENTA|\nNombre del cliente: {}\nNúmero de cliente: {}\nNúmero de producto: {}\n"\
            "Monto: {}\nFecha de apertura: {}\nFecha de acción: {}\nSucursal: {}\n"\
            "Estado: {}\nCorreo: {}\nTeléfono: {}".format(self.__nombre_cliente,
                                                            self.__numero_cliente,
                                                            self.__numero_producto,
                                                            self.__monto,
                                                            self.__fecha_apertura.strftime("%d-%m-%Y"),
                                                            self.__fecha_accion.strftime("%d-%m-%Y"),
                                                            self.__sucursal,
                                                            self.__estado,
                                                            self.__correo,
                                                            self.__telefono)

    def _iter_(self):
        """
        Método para devolver una representación iterable de una cuenta.
        :return: Representación iterable de una cuenta.
        :rtype: iterable
        """
        return iter(["Cuenta", self._nombre_cliente, self.numero_cliente, self._numero_producto,
                     self._monto, self.fecha_apertura, self.fecha_accion, self._sucursal,
                     self._estado, self.correo, self._estado])

if _name_ == "_main_":
    cuenta = Cuenta("Luis Francisco Revuelta", "000001", "12345678",
                    100000, "15-04-2023", "25-05-2023", 4, "Ciudad de México",
                    "luisfrancis@gmail.com", "5534689876")
    print(cuenta)
from locale import currency
from locale import setlocale
from locale import LC_MONETARY
import random

class Ejecutivo:
    def _init_(self, nombre, numero, rfc, direccion, telefono, sueldo):
        """
        Método constructor para manejar empleados que son ejecutivos de cuenta.
        :param str nombre: El nombre completo del empleado.
        :param str numero: El número de empleado del ejecutivo.
        :param str rfc: EL RFC del empleado.
        :param str direccion: La dirección del empleado.
        :param str telefono: El número de teléfono del empleado.
        :param str sueldo: El sueldo mensual del empleado.
        """
        self.__nombre = nombre
        self.__numero = numero
        self.__rfc = rfc
        self.__direccion = direccion
        self.__telefono = telefono
        self.__sueldo = sueldo

    #GETTERS
    @property
    def nombre(self):
        """
        Método para obtener el nombre del empleado.
        :return: El nombre completo del empleado.
        :rtype: str
        """
        return self.__nombre

    @property
    def numero(self):
        """
        Método para obtener el número de empleado del ejecutivo.
        :return: Número de empleado.
        :rtype: str
        """
        return self.__numero

    @property
    def rfc(self):
        """
        Método para obtener el RFC del ejecutivo.
        :return: RFC del ejecutivo.
        :rtype: str
        """
        return self.__rfc

    @property
    def direccion(self):
        """
        Método para obtener la dirección del empleado.
        :return: Dirección del empleado.
        :rtype: str
        """
        return self.__direccion

    @property
    def telefono(self):
        """
        Método para obtener el teléfono del ejecutivo.
        :return: Número de teléfono del ejecutivo.
        :rtype: str
        """
        return self.__telefono

    @property
    def sueldo(self):
        """
        Método para obtener el sueldo del ejecutivo.
        :return: Sueldo del ejecutivo.
        :rtype: str
        """
        return self.__sueldo

    #SETTERS
    @nombre.setter
    def nombre(self, nombre:str):
        """
        Método para establecer el nombre del empleado.
        :param nombre: El nombre del empleado.
        """
        self.__nombre = nombre

    @numero.setter
    def numero(self, numero:str):
        """
        Método para establecer el número de empleado del ejecutivo.
        :param numero: Número de empleado del ejecutivo.
        """
        self.__numero = numero

    @rfc.setter
    def rfc(self, rfc:str):
        """
        Método para estalecer el RFC del empleado.
        :param rfc: RFC del empleado.
        """
        self.__rfc = rfc

    @direccion.setter
    def direccion(self, direccion:str):
        """
        Método para establecer la dirección del empleado.
        :param direccion: La direccion del empleado.
        """
        self.__direccion = direccion

    @telefono.setter
    def telefono(self, telefono:str):
        """
        Método para establecer el número de teléfono del empleado.
        :param telefono: Número de teléfono del empleado.
        """
        self.__telefono = telefono

    @sueldo.setter
    def sueldo(self, sueldo:str):
        """
        Método para establecer el sueldo del ejecutivo.
        :param sueldo: Sueldo del ejecutivo.
        """
        self.__sueldo = sueldo


    #Método STR
    def _str_(self):
        """
        Método para imprimir un empleado como cadena.
        :return: Un empleado en formato de cadena.
        :rtype: str
        """
        setlocale(LC_MONETARY, "en_US")
        return "Ejecutivo de cuenta: \nNombre: {}\nNúmero de empleado: {}\n"\
            "RFC: {}\nDirección: {}\nTeléfono: {}\nSueldo: {}".format(self.__nombre,
                                                                          self.__numero,
                                                                          self.__rfc,
                                                                          self.__direccion,
                                                                          self.__telefono,
                                                                          currency(self.__sueldo, grouping=True))

    def _iter_(self):
        """
        Método para devolver una representación iterable de un ejecutivo.
        :return: Representación iterable de un ejecutivo.
        :rtype: iterable
        """
        setlocale(LC_MONETARY, "en_US")
        return iter(["Ejecutivo", self._nombre, self.numero, self._rfc,
                     self._direccion, self.telefono, currency(self._sueldo, grouping=True)])



if _name_ == "_main_":
    setlocale(LC_MONETARY, "en_US")
    ejecutivo = Ejecutivo("Ahmed Palomino Olivares", "105487",
                          "HZQE411228IX3", "Severino Ceniceros No. 8 No. 15, Barrio los Reyes Tláhuac, CDMX",
                          "5576913647", 40000.00)

    print(ejecutivo)
    
