import os

import mysql.connector


def obtener_conexion(database: str | None = None):
    default_database = os.getenv("DB_NAME", "bd_estudiante")
    candidates = []
    for candidate in (database, default_database, "bd_estudiante", "estudiante"):
        if candidate and candidate not in candidates:
            candidates.append(candidate)

    last_error = None
    for candidate in candidates:
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "127.0.0.1"),
                port=int(os.getenv("DB_PORT", "3306")),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", ""),
                database=candidate,
            )
        except mysql.connector.Error as exc:
            last_error = exc

    raise last_error or RuntimeError("No se pudo establecer la conexión con la base de datos.")
