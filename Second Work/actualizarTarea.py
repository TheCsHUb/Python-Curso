Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]

def Actualizar(listares):
    while True:
     codigo_encontrado = []   
     try:
        codigo = int(input("Introduzca el codigo correspondiente a la tarea: "))
        IndexLista = -1
        for d in listares:
            IndexLista = IndexLista + 1
            if d.get("Codigo") == codigo:
                   print("Tarea encontrada \n")
                   print(codigo_encontrado)
                   print("Escoja una de las siguinetes opciones: \n")
                   print("1--------------------------Actualizar titulo \n2--------------------------Actualizar descripcion\n3--------------------------Actualizar Status\n4--------------------------Salir")
                   while True:
                     try:
                      accion = int(input("Introduzca accion a realizar: "))
                      if 5 > accion > 0:
                       while True:
                           
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------ 
                        #------------------------------------------------Actualizar Titulo---------------------------------------------------------------     
                        if accion == 1:
                           try:
                               
                            Nuevo_titulo = input("Introduzca el nuevo titulo: ")
                            d["Titulo"] = Nuevo_titulo
                            print('Titulo Actualizado')
                            break
                           except:
                               print("No puede dejar el campo vacio")
                               continue
                        
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------ 
                        #------------------------------------------------Actualizar Descripcion---------------------------------------------------------------
                         
                        if accion == 2:
                            try: 
                                Nueva_Descripcion = input("Introduzca la nueva descripcion: ")
                                d["Descripcion"] = Nueva_Descripcion
                                print('Descripcion Actualizada')
                                break
                            except:
                                print("No puede dejar el campo vacio")
                                continue
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------
                        #------------------------------------------------------------------------------------------------------------------------ 
                        #------------------------------------------------Actualizar Status---------------------------------------------------------------
                         
                        if accion == 3:
                           Finalizado = False
                           while True:
                            if Finalizado == True:
                                break     
                            print("Introduzca el status de la tarea: \n------ 1 para completado ----------\n------ 2 para pendiente -------------- ")
                            Nuevo_Status = input("Status de la tarea: ")
                            if not Nuevo_Status:
                             print("Error. No puede dejar el campo vacio")
                             continue
                            elif Nuevo_Status: 
                                try: 
                                    Nuevo_Status = int(Nuevo_Status)
                                    if Nuevo_Status == 1 or Nuevo_Status == 2:
                                        if Nuevo_Status == 1:
                                            d["Status"] = "Completado"
                                            print("Status actualizado")
                                            Finalizado = True
                                            break
                                        else:
                                            d["Status"] = "Pendiente"
                                            print("Status actualizado")
                                            Finalizado = True
                                            break
                                    else:
                                        print("Solo se permite uno de los numeros indicados")
                                        Nuevo_Status = input("Status de la tarea: ")
                                        continue
                                    break
                                except Exception as e:
                                    print("Solo se permiten numeros enteros! \n")
                                    Nuevo_Status = input("Status de la tarea: ")
                                    continue
                                break
                            
                            break
                        if accion == 4:
                            break
                       break
                      else:
                         print("Solo se permite uno de los numeros proveeidos")
                         continue
                     
                     except:
                      print("Solo se permite numeros enteros!")
                      continue
                   break
            elif IndexLista == len(listares) - 1:
                print("Tarea no encontrada")
                break
        break             
     except Exception as e:
        print("Solo puedes introducir numeros")
        continue

#Actualizar(Tareas)         