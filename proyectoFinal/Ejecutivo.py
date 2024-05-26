#Programa: Ejecutivo.py
#Objetivo: Programa que define una clase para manejar ejecutivos de cuenta.
#Autor: Binary Balance
#Fecha: 23/05/24

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
