from colorama import Fore, Style, init

from src.comun.ambientes_enum import Ambientes

def mostrar_bienvenida():
    print(Fore.GREEN + "*" * 62)
    print("*" + " " * 60 + "*")
    print("*" + " " * 16 + Fore.CYAN + "Bienvenido a py-sql-executor" + Fore.GREEN + " " * 16 + "*")
    print("*" + " " * 60 + "*")
    print("*" * 62 + Style.RESET_ALL)


def seleccionar_ambiente(ambientes: list)-> str:
    if not (ambientes):
        print("No existen ambiente para seleccionar")
        return None    
    print("Por favor selecciona un ambiente:")
    for idx, opcion in enumerate(ambientes):
        print(f"{idx + 1}. {opcion}")
    while True:
        try:
            seleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= seleccion <= len(ambientes):
                print(f"\nHas seleccionado: {ambientes[seleccion - 1]}")
                return ambientes[seleccion - 1]
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def seleccionar_ambiente_configurar_nuevo(ambientes_disponibles: list) -> str:
    print("Por favor selecciona ambiente:")
    ambientes_disponibles.append("Agregar nuevo")
    for idx, opcion in enumerate(Ambientes.listar_nombres_ambiente()):
        print(f"{idx + 1}. {opcion}")
    
    while True:
        try:
            seleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= seleccion <= len(Ambientes):
                ambiente_seleccionado = list(Ambientes)[seleccion - 1]
                print(f"\nHas seleccionado: {ambiente_seleccionado.name}")
                return ambiente_seleccionado.name 
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def seleccionar_ambiente_configurar() -> str:
    print("Por favor selecciona un ambiente:")
    
    for idx, opcion in enumerate(Ambientes.listar_nombres_ambiente()):
        print(f"{idx + 1}. {opcion}")
    
    while True:
        try:
            seleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= seleccion <= len(Ambientes):
                ambiente_seleccionado = list(Ambientes)[seleccion - 1]
                print(f"\nHas seleccionado: {ambiente_seleccionado.name}")
                return ambiente_seleccionado.name 
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


