import sqlite3
import pymysql
from persistencia.crear_bd import crear_tablas
from menus.menuPrincipal import menu_principal  # <-- Mantenemos tu importación
from menu_usuario import solicitar_login

def main():
    try:
        crear_tablas()
    except (sqlite3.Error, pymysql.MySQLError, ValueError) as e:
        print(f"No fue posible conectarse a la base de datos: {e}")
        print("Revise la configuración del archivo .env e intente de nuevo.")
        return

    print("Base de datos preparada correctamente.")
    
    try:
        while True:
            # 1. Pide el login de inmediato al iniciar
            usuario_actual = solicitar_login()
            
            if usuario_actual is None:
                if input("Presiona Enter para reintentar o '0' para salir: ") == "0":
                    break
                continue
            
            # 2. Si el login es exitoso, lanzamos tu menú principal (pasándole el usuario actual si lo requiere)
            # O si prefieres mantener tu menu_principal() tal como lo tenías:
            menu_principal()
            
            usuario_actual = None  # Cierra la sesión al salir
            print("Sesión cerrada. Ingrese nuevamente.\n")
            
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma cerrado.")

if __name__ == "__main__":
    main()
