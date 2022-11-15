def leer_archivo(file_name):
    print(f'intentas abrir este arcivo {file_name}')
    #Abrir open
    #Procesar read/write
    #Cerrar close()
    #With nos permite agrupar trabajo con archivos
    with open(file_name, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            print(linea, end=' ')
        #while(linea):
         #   print(linea)
          #  linea = file.readline()

    #print('Archivo leido y cerrado')

def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
         file.write(f"\n{equipo}")

    print("equipo guardado")

def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos = file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("Equipo Eliminado!")
        with open(file_name, 'w') as file:
            file.writelines(lista_equipos)
    except ValueError:
        print('El equipo que deseas eliminar no existe')