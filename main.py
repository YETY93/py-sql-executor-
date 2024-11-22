
from colorama import init

from src.comun import constantes
from src.config import propiedades_ambiente
from src.menu.menu import mostrar_bienvenida, seleccionar_ambiente, seleccionar_ambiente_configurar, seleccionar_ambiente_configurar_nuevo
from src.menu.menu_creacion_ambien import crear_configuracion_ambiente
from src.models.configuracion_model import Configuracion
from src.utils.validator.validar_ambientes import ambientes_diponibles, configuracion_completa


# Inicializar colorama
init()



def main():
    mostrar_bienvenida()
    ambientes:list = configuracion_completa()
    ambientes_configurados:list = ambientes_diponibles()
   
    if ambientes:
        ambiente_seleccionado: str = seleccionar_ambiente(ambientes)
        # ejecutar ambiente
    else:
        if ambientes_configurados:
            ambiente: str = seleccionar_ambiente_configurar_nuevo(ambientes_configurados)
            if ambiente not in ambientes_configurados:
                crear_configuracion_ambiente(ambiente)

            configuracion_cargada: Configuracion = propiedades_ambiente.cargar_ambiente(constantes.path_ambientes, ambiente)
            print(configuracion_cargada)

        else:
            print("\n *** No hay ambientes configurados *** \n")
            ambiente: str = seleccionar_ambiente_configurar()
            crear_configuracion_ambiente(ambiente)

if __name__ == "__main__":
    main()