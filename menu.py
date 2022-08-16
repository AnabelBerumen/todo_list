from logger_base import log
from tareas import Tarea
from tareas_DAO import TareasDAO

opc = None

while opc != 5:
    print("""Opciones:
    1.- Listar Tareas
    2.- Agregar Tarea
    3.- Modificar tarea
    4.- Eliminar tarea
    5- Salir""")
    opc = int(input('Ingresa una opcion (1-5)' ))

    if opc == 1:
        tareas = TareasDAO.read()
        for tarea in tareas:
            log.debug(tarea)
    elif opc == 2:
        tarea_nueva = input('Escribe una tarea pendiente')
        tarea = Tarea(tarea_nueva)
        tareas_agregadas = TareasDAO.create(tarea)
        log.info(f'Tarea creada {tareas_agregadas}')
    elif opc == 3:
        id_tarea = int(input('Escribe el id de la tarea: '))
        tarea_var = input("Escribe la tarea a modificar: ")
        estado = input('Escribe el estado de la tarea: pendiente/completada: ')
        tarea = Tarea(id_tarea, tarea_var, estado)
        tarea_actualizada = TareasDAO.update(tarea)
        log.info(f'Tarea actualizada: {tarea_actualizada}')
    elif opc == 4:
        id_eliminar = int(input('Escribe el id_tarea a eliminar'))
        tarea = Tarea(id_tarea=id_eliminar)
        tarea_eliminada = TareasDAO.delete(tarea)
        log.info(f'Tarea eliminada {tarea_eliminada}')
else:
    log.info('Salimos de la aplicación...')