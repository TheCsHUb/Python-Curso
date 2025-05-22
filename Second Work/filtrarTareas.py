Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]


def Filtrar(listares):
    while True:
        
            print("-----------------------------------------------------------------Seleccione uno de las acciones proveidas-------------------------------------------------------------------\n")
            print("1-------------------------------------------------------Filtrar tareas por titulo\n2-------------------------------------------------------Salir")
            opcion = input("Introduce opcion: ")
            if not opcion:
                print("No puede dejar el campo vacio")
                continue
            else:
                while True:
                    
                    try:
                        opcion = int(opcion)
                        if opcion == 1:
                            print("--------------------------------------------------Filtrar por titulo----------------------------------------------------------- \n \n")
                            titulo = []
                            titulo = input("Introduzca titulo:  ")
                            if not titulo:
                             print("No puede dejar el campo vacio")
                             continue
                            else: 
                                
                                matching_dicts = [d for d in Tareas if titulo.lower() in d["Titulo"].lower()]
                                print(matching_dicts)
                                if matching_dicts != []:
                                        print(matching_dicts)
                                        break
                                else:
                                        print("No se encontro titulo!")
                                        break
                            
                                
                        else:
                            break     
                    except Exception as e:
                        print("Solo se permite numeros enteros!")
                        continue

            break
#Filtrar(Tareas)