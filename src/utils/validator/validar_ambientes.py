from src.utils import utils
from src.comun import constantes
from src.comun.ambientes_enum import Ambientes


def validar_local()-> bool:
    print( utils.existe_archivo(constantes.path_ambientes + Ambientes.LOCAL.value))
    return utils.existe_archivo(constantes.path_ambientes + Ambientes.LOCAL.value)


def validar_qa()-> bool:
    print( utils.existe_archivo(constantes.path_ambientes + Ambientes.QA.value))
    return utils.existe_archivo(constantes.path_ambientes + Ambientes.QA.value)

    
def validar_prod()-> bool:
    print( utils.existe_archivo(constantes.path_ambientes + Ambientes.PROD.value))
    return utils.existe_archivo(constantes.path_ambientes + Ambientes.PROD.value)
    
def configuracion_completa()-> list | None:
    if(validar_local() and validar_qa() and validar_prod() ):
        return [Ambientes.LOCAL.name, Ambientes.QA.name, Ambientes.PROD.name]
    return []

def ambientes_diponibles()-> list:
    ambientes: list = []
    if(validar_local()):
        ambientes.append(Ambientes.LOCAL.name)
    elif(validar_qa()):
        ambientes.append(Ambientes.QA.name)
    elif(validar_prod()):
        ambientes.append(Ambientes.PROD.name)
    return ambientes

def ambientes_faltantes(ambientes: list)-> list:
    ambiente_faltante: list = []
    if Ambientes.LOCAL.name not in ambientes:
        ambiente_faltante.append(Ambientes.LOCAL.name)
    elif Ambientes.QA.name not in ambientes:
        ambiente_faltante.append(Ambientes.QA.name)
    elif Ambientes.PROD.name not in ambientes:
        ambiente_faltante.append(Ambientes.PROD.name)
    return ambiente_faltante