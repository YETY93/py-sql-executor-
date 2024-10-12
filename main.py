
from colorama import init
from src.menu.menu import mostrar_bienvenida, seleccionar_ambiente, seleccionar_ambiente_configurar, seleccionar_ambiente_configurar_nuevo
from src.menu.menu_creacion_ambien import crear_configuracion_ambiente
from src.utils.validator.validar_ambientes import ambientes_diponibles, configuracion_completa


# Inicializar colorama
init()



def main():
    mostrar_bienvenida()
    ambientes:list = configuracion_completa()
    ambientes_configurados:list = ambientes_diponibles()
   
    if(ambientes_configurados):
        seleccionar_ambiente(ambientes)
        # ejecutar ambiente
    else:
        if(ambientes_configurados):
            ambiente = seleccionar_ambiente_configurar_nuevo(ambientes_configurados)
            crear_configuracion_ambiente(ambiente)
        else:
            print("\n *** No hay ambientes configurados *** \n")
            ambiente: str = seleccionar_ambiente_configurar()
            crear_configuracion_ambiente(ambiente)

if __name__ == "__main__":
    main()