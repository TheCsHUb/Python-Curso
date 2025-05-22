Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]

def Add_Tarea(listares):
    tarea = {}
    print("--------------------------------------------Añadir Tarea----------------------------------------------------")
    #-------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------Codigo-----------------------------------------------------------
    
    while True:
        
     try:
        codigo = int(input('Codigo de la tarea: '))
        tarea['Codigo'] = codigo
        break
     except Exception as e:
        print("Solo puede introducir numeros enteros!")
        continue
    #-------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------Titulo-----------------------------------------------------------
    titulo = input("Introduce el titulo: ")
    while True:
     if not titulo:
         print("Error. No puede dejar el campo vacio")
         titulo = input("Introduce el titulo: ")
         continue
     elif len(titulo) >= 20:
        print("EL titulo solo puede tener maximo 20 caracteres")
        titulo = input("Introduce el titulo: ")
        continue
     else:
        tarea["Titulo"] = titulo
        break
    #-------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------Descripcion-----------------------------------------------------------
    
    Descripcion = input("Introduce la descripcion: ")
    while True:
        if not Descripcion:
         print("Error. No puede dejar el campo vacio")
         Descripcion = input("Introduce la descripcion: ")
         continue
        else:
            tarea["Descripcion"] = Descripcion
            break
    #-------------------------------------------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------------------------------------------
    #--------------------------------------------------------------Status-----------------------------------------------------------
    
    
    while True:     
        print("Introduzca el status de la tarea: \n------ 1 para completado ----------\n------ 2 para pendiente -------------- ")
        Status = input("Status de la tarea: ")
        if not Status:
         print("Error. No puede dejar el campo vacio")
         Status = input("Status de la tarea: ")
         continue
        else: 
            try: 
                Status = int(Status)
                if Status == 1 or Status == 2:
                    if Status == 1:
                        tarea["Status"] = "Completado"
                        break
                    else:
                        tarea["Status"] = "Pendiente"
                        break
                else:
                    print("Solo se permite uno de los numeros indicados")
                    Status = input("Status de la tarea: ")
                    continue
            except Exception as e:
                print("Solo se permiten numeros enteros! \n")
                Status = input("Status de la tarea: ")
                continue
    print("\n \n Tarea añadida exitosamente!")            
    print(tarea)
    listares.append(tarea)    
  

#Add_Tarea(Tareas)