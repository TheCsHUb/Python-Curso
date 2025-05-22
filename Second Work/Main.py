from añadirTarea import Add_Tarea 
from filtrarTareas import Filtrar
from ListadodeTares import Listado
from actualizarTarea import Actualizar
from eliminarTarea import eliminar

ListadoDeOpciones = ['1 ----------------------------------- Lista de tareas \n', 
                     '2 ----------------------------------- Filtrar tateas \n',
                     '3 ----------------------------------- Añadir tarea \n',
                     '4 ----------------------------------- Actualizar tarea \n',
                     '5 ----------------------------------- Eliminar tarea \n',
                     '6 ----------------------------------- Salir \n'
                     ]
Tareas = [{'Codigo': 15432, 'Titulo': 'Actualizar base de datos', 'Descripcion': 'Actualizar la base de datos SQL', "Status": "Completado"},
          {'Codigo': 45618, 'Titulo': 'Mejorar el UI de la pagina web', 'Descripcion': 'Cambiar el diseño de la pagina web a algo mas moderno', "Status": "Pendiente"},
          {'Codigo': 21004, 'Titulo': 'Remover codigo obsoleto', 'Descripcion': 'Remover codigo que ha sido mejorado o que tiene dependencias obsoletas', "Status": "Completado"}]


Opciones = ", ".join(ListadoDeOpciones)

def Main(Lista_Tareas):
    while True:
      try:
        print('Bienvenido al programa de tareas \n\n')
        print(Opciones)
        Opcion = int(input("Eliga la accion que desea realizar: "))
        
        if Opcion == 1:
            Listado(Lista_Tareas)
            continue
        elif Opcion == 2:
            Filtrar(Lista_Tareas)
            continue
        elif Opcion == 3:
            Add_Tarea(Lista_Tareas)
            continue
        elif Opcion == 4:
            Actualizar(Lista_Tareas)
            continue
        elif Opcion == 5:
            eliminar(Lista_Tareas)
            continue
        elif Opcion == 6:
            break
        else:
         print("Solo se permite uno de los numeros proveeidos!")
      except Exception as e:
          print("Solo se permite numeros enteros")  
    
     
 
Main(Tareas)