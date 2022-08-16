from conexion import Conexion
from logger_base import log
from tareas import Tarea


class TareasDAO:
    _SELECT = 'SELECT * FROM task ORDER BY id_tarea'
    _INSERT = 'INSERT INTO task(tarea, estado) VALUES(%s,%s)'
    _UPDATE = 'UPDATE task SET tarea=%s, estado=%s WHERE id_tarea=%s'
    _DELETE = 'DELETE FROM task WHERE id_tarea=%s'

    @classmethod
    def create(cls, tareas):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (tareas.tarea, tareas.estado)
                cursor.execute(cls._INSERT, valores)
                return cursor.rowcount

    @classmethod
    def read(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall()
                tareas = []
                for registro in registros:
                    tarea = Tarea(registro[0], registro[1], registro[2])
                    tareas.append(tarea)
                return tareas

    @classmethod
    def update(cls, tarea):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (tarea.tarea, tarea.estado, tarea.id_tarea)
                cursor.execute(cls._UPDATE, valores)
                log.debug(f'Tarea actualizada: {tarea}')
                return cursor.rowcount

    @classmethod
    def delete(cls, tarea):
        with Conexion.obtenerConexion() as conexion:
            with Conexion.obtenerCursor() as cursor:
                valor = (tarea.id_tarea,)
                cursor.execute(cls._DELETE, valor)
                log.debug(f'Tarea eliminada {tarea}')
                return cursor.rowcount


if __name__ == '__main__':
    """ tareas1 = Tarea(tarea="Darle desayuno a las perras")
    tareas_nuevas = TareasDAO.create(tareas1)
    log.debug(f'Tareas nuevas {tareas_nuevas}')

    tareas1 = Tarea(id_tarea=4, tarea='Barrer el patio', estado='pendiente')
    tarea_actualizada = TareasDAO.update(tareas1)
    log.debug(f'Tarea actualizada: {tarea_actualizada}')
    
    tarea1 = Tarea(id_tarea=7)
    tareas_eliminadas = TareasDAO.delete(tarea1)
    log.debug(f'Tarea eliminada {tareas_eliminadas}')
    """

    tareas = TareasDAO().read()
    for tarea in tareas:
        log.debug(tarea)
