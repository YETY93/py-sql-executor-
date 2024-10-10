from enum import Enum

class Ambientes(Enum):
    QA = "qa.pkl"
    LOCAL = "local.pkl"
    PROD = "produccion.pkl"


    @staticmethod
    def listar_nombres_ambiente() -> list:
        """
        Retorna una lista con los nombres de los ambientes definidos en el Enum.
        
        Returns:
            list: Una lista con los nombres de los ambientes.
        """
        return [ambiente.name for ambiente in Ambientes]
    

    @staticmethod
    def obtener_valor(enum_ambiente: str) -> Enum:
        """
        Retorna el objeto Ambientes asociado al nombre del ambiente.
        
        Args:
            enum_ambiente (str): El nombre del ambiente.
        
        Returns:
            Enum: El objeto Ambientes correspondiente al nombre del ambiente.
        
        Raises:
            ValueError: Si el nombre del ambiente no es válido.
        """
        try:
            return getattr(Ambientes, enum_ambiente)
        except AttributeError:
            raise ValueError(f"'{enum_ambiente}' no es un ambiente válido. "
                             f"Ambientes disponibles: {Ambientes.listar_nombres_ambiente()}")