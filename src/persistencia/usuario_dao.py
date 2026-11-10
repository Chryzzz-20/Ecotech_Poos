from dominio.usuario import Usuario
from persistencia.base_dao import BaseDAO


class UsuarioDAO(BaseDAO):
    TABLA = "usuario"
    COLUMNAS = "id, id_empleado, nombre, contraseña, rol"
    NOMBRE = "el usuario"

    @staticmethod
    def _convertir(fila):
        return Usuario.desde_bd(
            id=fila[0],
            id_empleado=fila[1],
            nombre=fila[2],
            contraseña_cifrada=fila[3],
            rol=fila[4],
        )

    @classmethod
    def insertar(cls, usuario):
        sql = "INSERT INTO usuario (id_empleado, nombre, contraseña, rol) VALUES (?, ?, ?, ?)"
        parametros = (usuario.id_empleado, usuario.nombre, usuario.contraseña, usuario.rol)
        nuevo_id = cls._insertar(sql, parametros, "insertar el usuario")
        if nuevo_id is None:
            return None
        usuario.id = nuevo_id
        return usuario

    @classmethod
    def actualizar(cls, usuario):
        sql = "UPDATE usuario SET id_empleado = ?, nombre = ?, contraseña = ?, rol = ? WHERE id = ?"
        parametros = (usuario.id_empleado, usuario.nombre, usuario.contraseña, usuario.rol, usuario.id)
        return cls._ejecutar(sql, parametros, "actualizar el usuario") > 0

    @classmethod
    def buscar_por_nombre(cls, nombre):
        usuarios = cls._listar_donde("nombre = ?", (nombre,), "buscar el usuario")
        if not usuarios:
            return None
        return usuarios[0]


    @classmethod
    def buscar_por_empleado(cls, id_empleado):
        usuarios = cls._listar_donde(
            "id_empleado = ?", (id_empleado,), "buscar usuario por empleado"
        )
        if not usuarios:
            return None
        return usuarios[0]

@classmethod
    def insertar(cls, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            sql = """
                INSERT INTO usuario (nombre_usuario, password_hash, empleado_id)
                VALUES (:1, :2, :3)
            """
            cursor.execute(sql, (usuario.nombre_usuario, usuario.password_hash, usuario.empleado_id))
            conexion.commit()
            
            cursor.execute("SELECT MAX(id) FROM usuario WHERE nombre_usuario = :1", (usuario.nombre_usuario,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            conexion.rollback()
            print(f"Error al insertar usuario: {e}")
            raise e
        finally:
            cursor.close()
            conexion.close()

    @classmethod
    def buscar_por_nombre(cls, nombre_usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            sql = "SELECT id, nombre_usuario, password_hash, empleado_id FROM usuario WHERE nombre_usuario = :1"
            cursor.execute(sql, (nombre_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(nombre_usuario=row[1], password_hash=row[2], empleado_id=row[3], id=row[0])
            return None
        except Exception as e:
            print(f"Error al buscar usuario por nombre: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()