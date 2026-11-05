class Empleado:
    MIN_NOMBRE = 2
    MAX_NOMBRE = 100
    MIN_CORREO = 6
    MAX_CORREO = 254
    def __init__(self, nombre: str, direccion: str, telefono: int, correo: str, salario: int, inicioContrato: str, id_departamento: int = None, id = None):
        self.id = id
        self.id_departamento = id_departamento

        self.nombre = self.validar_nombre(nombre)
        self.direccion = direccion
        self.telefono = telefono
        self.correo = self.validar_correo(correo)
        
        self.salario = salario
        self.inicioContrato = inicioContrato

    def mostrar_datos(self) -> str:
        return f"\nId {self.id}, Nombre {self.nombre}, Correo {self.correo}"

    def actualizar_nombre(self, nombre):
        self.nombre = self.validar_nombre(nombre)

    def agregar_descripcion(self) -> str:
        return (f"Empleado {self.nombre} (ID {self.id}) - {self.correo}\n"
                f"Dirección: {self.direccion} | Teléfono: {self.telefono}\n"
                f"Salario: {self.salario} | Inicio contrato: {self.inicioContrato} | "
                f"Departamento: {self.id_departamento if self.id_departamento is not None else 'Sin departamento'}")

     @classmethod
    def validar_nombre(cls, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto.")
        
        nombre = nombre.strip()
            
        if not cls.MIN_NOMBRE <= len(nombre) <= cls.MAX_NOMBRE:
            raise ValueError(
                f"El nombre debe tener entre {cls.MIN_NOMBRE} "
                f"y {cls.MAX_NOMBRE} caracteres."
            )
           
            return nombre