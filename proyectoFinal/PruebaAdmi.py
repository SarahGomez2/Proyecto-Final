#Programa:Proyecto final 
#Objetivo: Crear menú principal de la institucion bancaria 
#Autor: Binary Balance
#Fecha: 26/05/2024
#Importamos las clases que ya tenemos 
import AdministracionCuentas as ad
#Creamos una lista vacia 
admin= ad.AdministracionCuentas() 
# Creamos el menú
def mostrar_menu():
    print("Seleccione apartado que quiera visitar")
    print("1) Cuentas")
    print("2) Ejecutivos")
    print("3) Generar reportes")
    print("4) Cerrar")
    accion= input("Selecciona una opcion: ")
    if accion not in "1234" or len(accion) !=1:
        print("Opción invalida \n") 
        continue 
    match accion: 
        case "1": 
            while True: 
                print("[C]argar información")
                print("C[O]nsultar") #Necesito ayuda para hacer el menu de consultas (inciso b, primeros 2 puntos
                while True: 
                    print("[N]úmero de cliente")
                    print([T]ipo de cuenta")
                    print(No[M]bre del cliente")
                    print(
                    
                
                
    

        
