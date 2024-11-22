from colorama import Fore, Style

from src.comun.enums.ambientes_enum import Ambiente_enum
from src.comun.enums.otro_ambiente_enum import Otro_ambiente

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
    print("Por favor selecciona un ambiente a ejecutar: ")
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


def seleccionar_ambiente_configurar_nuevo(ambientes_configurados: list) -> str:
    print("Por favor selecciona ambiente:")
    ambientes_configurados.append(Otro_ambiente.NUEVO.value)
    for idx, opcion in enumerate(ambientes_configurados):
        print(f"{idx + 1}. {opcion}")
    
    while True:
        try:
            seleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= seleccion <= len(ambientes_configurados):
                ambiente_seleccionado = ambientes_configurados[seleccion - 1]
                if(ambiente_seleccionado == Otro_ambiente.NUEVO.value):
                    pendientes: list = listar_ambientes_pendientes(Ambiente_enum.listar_nombres_ambiente(), ambientes_configurados)
                    return seleccionar_ambiente(pendientes)
                print(f"\nHas seleccionado: {ambiente_seleccionado}")
                return ambiente_seleccionado 
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def seleccionar_ambiente_configurar() -> str:
    print("Por favor selecciona un ambiente:")
    
    for idx, opcion in enumerate(Ambiente_enum.listar_nombres_ambiente()):
        print(f"{idx + 1}. {opcion}")
    
    while True:
        try:
            seleccion = int(input("\nIntroduce el número de la opción: "))
            if 1 <= seleccion <= len(Ambiente_enum):
                ambiente_seleccionado = list(Ambiente_enum)[seleccion - 1]
                print(f"\nHas seleccionado: {ambiente_seleccionado.name}")
                return ambiente_seleccionado.name 
            else:
                print("Selección no válida. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")


def listar_ambientes_pendientes(ambientes: list, ambientes_configurados: list) -> list:
    print("")