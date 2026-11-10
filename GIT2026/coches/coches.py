from mysql.connector import Error

from conexionBD import obtener_conexion

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._color = color
        self._marca = marca
        self._velocidad = velocidad
        self._modelo = modelo
        self._potencia = potencia
        self._asientos = asientos

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, value):
        self._velocidad = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, value):
        self._asientos = value


    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        self._velocidad -= 1

    @staticmethod
    def consultar():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "select id, marca, color, modelo, velocidad, potencia, asientos "
                "from coches order by id"
            )
            return cursor.fetchall()
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def consultar_por_id(id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "select id, marca, color, modelo, velocidad, potencia, asientos "
                "from coches where id = %s",
                (id,),
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("delete from coches where id = %s", (id,))
            conexion.commit()
            return cursor.rowcount > 0
        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()
            
    def insertar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "insert into coches "
                "(marca, color, modelo, velocidad, potencia, asientos) "
                "values (%s, %s, %s, %s, %s, %s)",
                (
                    self.marca,
                    self.color,
                    self.modelo,
                    self.velocidad,
                    self.potencia,
                    self.asientos,
                ),
            )
            conexion.commit()
            return True
        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()

    def actualizar(self, id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("select 1 from coches where id = %s", (id,))
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                "update coches set marca = %s, color = %s, modelo = %s, "
                "velocidad = %s, potencia = %s, asientos = %s where id = %s",
                (
                    self.marca,
                    self.color,
                    self.modelo,
                    self.velocidad,
                    self.potencia,
                    self.asientos,
                    id,
                ),
            )
            conexion.commit()
            return True
        except Error:
            conexion.rollback()
            raise
        finally:
            cursor.close()
            conexion.close()
