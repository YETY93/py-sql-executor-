class Configuracion:
    def __init__(self, user: str, password: str, host: str,  database: str ) -> None:
        self.user = user
        self.password = password
        self.host = host
        self.database = database