class Usuario:
    def __init__(self, nombre: str, contraseña: str, rol: str, id_empleado: int = None, id = None):
        self.id = id
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.contraseña = None
        self.rol = rol
        self._registrado = False
        self._establecer_contraseña(contraseña)

    @classmethod
    def desde_bd(cls, id, nombre: str, contraseña_cifrada: str, rol: str, id_empleado: int = None):
        usuario = cls.__new__(cls)
        usuario.id = id
        usuario.id_empleado = id_empleado
        usuario.nombre = nombre
        usuario.contraseña = contraseña_cifrada
        usuario.rol = rol
        usuario._registrado = True
        return usuario
        
    def _establecer_contraseña(self, contraseña: str) -> None:
        from dominio.controlAcceso import ControlAcceso
        if not contraseña or len(contraseña) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres")
        self.contraseña = ControlAcceso.cifrar_contraseña(contraseña)

    def registrar(self) -> bool:
        if not self.nombre or not self.contraseña or not self.rol:
            return False
        self._registrado = True
        return True
 
    def iniciar_sesion(self, contraseña_ingresada: str) -> bool:
        from dominio.controlAcceso import ControlAcceso
        if not self._registrado:
            return False
        return ControlAcceso.validar_credenciales(self, contraseña_ingresada)

class Usuario:
    MIN_USUARIO = 3
    MAX_USUARIO = 40
    MIN_CLAVE = 6

    def __init__(self, nombre_usuario, password_hash, empleado_id, id=None):
        if type(empleado_id) is not int or empleado_id <= 0:
                raise ValueError("El ID del empleado debe ser positivo.")
        self.id = id
        self.empleado_id = empleado_id
        self.nombre_usuario = self.normalizar_usuario(nombre_usuario)
        self.password_hash = password_hash

@classmethod
def normalizar_usuario(cls, nombre):
    if not isinstance(nombre, str):
        raise TypeError("El usuario debe ser texto.")
    nombre = nombre.strip().lower()
    if not cls.MIN_USUARIO <= len(nombre) <= cls.MAX_USUARIO:
        raise ValueError("Usuario fuera del largo permitido.")
    if not all(c.isascii() and (c.isalnum() or c == "_")
            for c in nombre):
        raise ValueError("Use letras ASCII, números o guion bajo.")
    return nombre

def validar_clave(cls, clave):
    if not isinstance(clave, str):
        raise TypeError("La contraseña debe ser texto.")
    if len(clave) < cls.MIN_CLAVE:
        raise ValueError(
            f"Use al menos {cls.MIN_CLAVE} caracteres."
        )
    return clave # Sin strip, lower ni truncado.