from logger_base import log

class Tarea:
    def __init__(self, id_tarea=None, tarea=None, estado='pendiente'):
        self._id_tarea = id_tarea
        self._tarea = tarea
        self._estado = estado

    def __str__(self):
        return f'''
            Id Tarea: {self._id_tarea}, Tarea: {self._tarea}.
            Estado: {self._estado}.
        '''

    @property
    def id_tarea(self):
        return self._id_tarea

    @id_tarea.setter
    def id_tarea(self, id_tarea):
        self._id_tarea = id_tarea

    @property
    def tarea(self):
        return self._tarea

    @tarea.setter
    def tarea(self, tarea):
        self._tarea = tarea

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, estado):
        self._estado = estado


if __name__ == '__main__':
    tarea1 = Tarea(1, 'Lavar la ropa', 'pendiente')
    log.debug(tarea1)