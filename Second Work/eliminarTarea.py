Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]

def eliminar(listares):
   while True: 
    try:
        codigo = int(input("Introduzca el codigo de la tarea que desea eliminar: "))
        for d in listares:
            if d['Codigo'] == codigo:
                listares.remove(d)
                print("Tarea removida exitsamente")
                break
            else:
                print("No se encontro una tarea con ese codigo")
                break
        break
    except:
        print("Solo puede introducir numeros enteros")
        continue