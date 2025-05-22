Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]


def Listado(listares):
    

    while True:
        print('------------------------------------Listado de tareas------------------------------------------------ \n \n')
        print('1 ----------------------- Completadas \n2 ----------------------- Pendientes \n3 ----------------------- Atras')
        opcion = input('Elija una opcion: ')
        if not opcion:
            print("No puede dejar el campo vacio")
            continue
        else: 
         try:
            opcion = int(opcion)
            if 4 > opcion > 0:
                if opcion == 1:
                 Listado_filtrado = [l for l in listares if l.get('Status') == 'Completado']
                 print(Listado_filtrado)
                 continue
                elif opcion == 2:
                 Listado_filtrado = [l for l in listares if l.get('Status') == 'Pendiente']
                 print(Listado_filtrado)
                 continue
                elif opcion == 3:
                    break
                
            else:
                print('Solo se permite una de la acciones proveidas. Pruebe de nuevo \n')
                continue 
        
         except Exception as e:
            
            print("Solo se puede introducir numeros enteros")
            continue

    

#Listado(Tareas)
    


