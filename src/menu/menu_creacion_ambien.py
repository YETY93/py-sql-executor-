from enum import Enum
import getpass
from src.comun import constantes
from src.comun.ambientes_enum import Ambientes
from src.models.configuracion import Configuracion
from src.utils.administrar_configuracion import persistir_configuracion_ambiente  # Para ingresar contraseñas sin mostrarlas por consola

def crear_configuracion_ambiente(tipo_ambiente: str)-> Configuracion:
    """
    Crea una nueva configuración de ambiente basada en la entrada del usuario.

    Args:
        ambiente (str): El nombre del ambiente.

    Returns:
        Configuracion o None: La configuración creada si todo es válido, None si el ambiente está vacío.
    """
    if not tipo_ambiente:
        print("El ambiente no puede estar vacío.")
        return None

    try:
        usuario = input("Ingrese el nombre de usuario de la base de datos: ")
        contrasena = getpass.getpass("Ingrese la contraseña: ")
        host = input("Ingrese la URL del host de la base de datos: ")
        base_datos = input("Ingrese el nombre de la base de datos: ")
        config = Configuracion(usuario, contrasena, host, base_datos)
        valido = mostrar_configuracion(config)

        if not valido:
            return crear_configuracion_ambiente(tipo_ambiente)
        else:
            persistir_configuracion_ambiente(tipo_ambiente, config)
            return config
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

def mostrar_configuracion(config: Configuracion) -> bool:
    print("****************************************")
    print("\nLa configuración es:")
    print(f"Usuario: {config.user}")
    print(f"Host: {config.host}")
    print(f"Base de datos: {config.database}")
    
    while True:
        print("\n¿La configuración del ambiente es correcta?")
        print("1. Sí")
        print("2. No")
        
        opcion = input("Seleccione una opción (1 o 2): ").strip()
        
        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Por favor seleccione 1 o 2.")
 

