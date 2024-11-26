from src.comun import constantes
from src.comun.enums.ambientes_enum import Ambiente_enum
from src.utils import utils


def validar_local()-> bool:
    return utils.existe_archivo(constantes.path_ambientes + Ambiente_enum.LOCAL.value)


def validar_qa()-> bool:
    return utils.existe_archivo(constantes.path_ambientes + Ambiente_enum.QA.value)


def validar_prod()-> bool:
    return utils.existe_archivo(constantes.path_ambientes + Ambiente_enum.PROD.value)

def configuracion_completa()-> list | None:
    if(validar_local() and validar_qa() and validar_prod() ):
        return [Ambiente_enum.LOCAL.name, Ambiente_enum.QA.name, Ambiente_enum.PROD.name]
    return []

def ambientes_diponibles()-> list:
    ambientes: list = []
    if(validar_local()):
        ambientes.append(Ambiente_enum.LOCAL.name)
    if(validar_qa()):
        ambientes.append(Ambiente_enum.QA.name)
    if(validar_prod()):
        ambientes.append(Ambiente_enum.PROD.name)
    return ambientes

def ambientes_faltantes(ambientes: list)-> list:
    ambiente_faltante: list = []
    if Ambiente_enum.LOCAL.name not in ambientes:
        ambiente_faltante.append(Ambiente_enum.LOCAL.name)
    elif Ambiente_enum.QA.name not in ambientes:
        ambiente_faltante.append(Ambiente_enum.QA.name)
    elif Ambiente_enum.PROD.name not in ambientes:
        ambiente_faltante.append(Ambiente_enum.PROD.name)
    return ambiente_faltante
