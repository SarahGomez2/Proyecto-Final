# Programa: proyecto final.py
 # Objetivo: Hacer puntos 7, 8 y 9 del proyecto final. 
    # 7. Dar de alta una nueva cuenta
    # 8. Registrar una nueva apertura de cuenta 
    # 9. Dar de alta nuevo empleado
 # Autor: Binary Balance
 # Fecha: 12/05/2024


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
