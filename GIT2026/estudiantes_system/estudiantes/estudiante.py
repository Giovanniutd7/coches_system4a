from mysql.connector import Error

if __package__ == "estudiantes_system.estudiantes":
    from estudiantes_system.conexionBD import obtener_conexion
else:
    from conexionBD import obtener_conexion

class Estudiantes:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def insertar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "insert into estudiante (nombre, nota) values (%s, %s)",
                (self.nombre, self.nota),
            )
            conexion.commit()
            return True

        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def consultar():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("select id, nombre, nota from estudiante order by id")
            return cursor.fetchall()

        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id_estudiante):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("delete from estudiante where id = %s", (id_estudiante,))
            conexion.commit()
            return cursor.rowcount > 0

        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def actualizar(self, id_estudiante):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("select 1 from estudiante where id = %s", (id_estudiante,))
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                "update estudiante set nombre = %s, nota = %s where id = %s",
                (self.nombre, self.nota, id_estudiante),
            )
            conexion.commit()
            return True

        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()
