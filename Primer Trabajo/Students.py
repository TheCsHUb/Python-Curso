
program_on = True
counter = 1

Estudiantes = [{'nombre': 'antonio',
                'apellido': 'Guzman',
                'cedula': '3',
                'nota1': 18, 
                'nota2': 19, 
                'nota3': 17,
                'prodemdio': 18},]

Datos = ['nombre', 'apellido', 'cedula', 'nota1', 'nota2', 'nota3',]

mensajeEntrada = '''Bienvenido. Presione el numero correspondiente a la accion que quiere realizar: \n 
                    1 ---------- Lista de estudiantes \n
                    2 ---------- Registrar estudiante \n
                    3 ---------- Eliminar estudiante \n
                    4 ---------- Salir del programa \n
                   '''


while program_on == True:
    
    #Entrada al programa
    print(mensajeEntrada)
     
    accion = int(input('Indique accion: '))
    
    
    #Asegurarse que numeros proveidos son los indicados
    if type(accion) != int or accion > 5 and accion < 1 or accion == False:
        print('Solo se permite usar uno de los numeros indicados')
    
    else:
        #==================================================Lista De Estudiantes====================================================================
        if accion == 1:
            print(Estudiantes)
        
        
        #==================================================Agregar Un Estudiante===================================================================
        elif accion == 2:
            nota_cumulativa = 0
            nuevo_estudiante   = {}
            print('Introdusca datos del estudiante:\n')
            for dato in Datos:   
              while True:
                dato_nuevo = input(dato + ': ')
                 
                
                
                
                
                
                
                
                #=======================================================Notas========================================================================
                if dato == 'nota1' or dato == 'nota2' or dato == 'nota3':
                    try:
                        dato_nuevo = float(dato_nuevo)
                        if 0 < dato_nuevo <= 20:
                           nota_cumulativa += dato_nuevo
                           nuevo_estudiante[dato] = dato_nuevo
                           break
                        else:
                            print('Solo se permite numeros del 0 al 20')
                            
                    except:
                        print('\n ¡Solo se pueden numeros! \n')
                        
                        
                        
                        
                        
                        
                #=======================================================Cedula=======================================================================
                elif dato == 'cedula':
                    try:
                        dato_nuevo = float(dato_nuevo)
                        if dato_nuevo % 1 == 0:
                          nuevo_estudiante[dato] = int(dato_nuevo)
                          break
                        else:
                          print('\n ¡Solo se permite numeros enteros! \n')
                          
                    except:
                         print('\n ¡Solo se permite numeros! \n')
                         
                        
                #=======================================================Nombre======================================================================
                elif dato == 'nombre' or dato == 'apellido':
                    while True:
                     try:
                        dato_nuevo = float(dato_nuevo)
                        print('Solo puede proveer nombres!')
                        dato_nuevo = input(dato + ': ')
                     except:
                      if len(dato_nuevo) == 0:
                          print('no puede dejar el campo vacio!')
                          dato_nuevo = input(dato + ': ')     
                      else: 
                          nuevo_estudiante[dato] = dato_nuevo
                          break
                        
                    break
                    
                    
            
            nuevo_estudiante['promedio'] = nota_cumulativa / 3
            Estudiantes.append(nuevo_estudiante)
            print('\n Estudiante añadido! \n')    
            
        
        
        
        
        
        #=========================================================Borrar Un Estudiante==============================================================        
        elif accion == 3:
            
            print('Ingrese cedula del estudiante que desea eliminar')
            while True:
                
                del_estud = input('Cedula: ')
                try:
                    del_estud = float(del_estud)
                    if del_estud % 1 == 0:
                          
                          break
                    else:
                          print('\n ¡Solo se permite numeros enteros! \n')
                        
                          
                except:
                         print('\n ¡Solo se permite numeros! \n')
            
            
            for estud in Estudiantes:
                counter += 1
                del_estud = int(del_estud)
                print(estud['cedula'])
                print(del_estud)  
                if int(estud['cedula']) == del_estud:
                    Estudiantes.remove(estud)
                    print('\n Estudiante removido \n')
                    break 
                else:
                    if counter == len(Estudiantes) - 1:
                       print(' \n Cedula no esta registrada \n')
                        
         
         
         
         
         #========================================================Terminar Programa=================================================================   
        elif accion == 4:
            
            print('Programa terminado')
            program_on = False
    
    
    
    

