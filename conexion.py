import psycopg2 as psycopg2
from logger_base import log
import sys


class Conexion:
    conexion = None
    cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls.conexion is None:
            try:
                cls.conexion = psycopg2.connect(database="todo_db", user="postgres", password="admin", host="127.0.0.1", port="5432")
                log.debug(f'Conexion exitosa: {cls.conexion}')
                return cls.conexion
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        else:
            return cls.conexion


    @classmethod
    def obtenerCursor(cls):
        if cls.cursor is None:
            try:
                cls.cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls.cursor}')
                return cls.cursor
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls.cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()