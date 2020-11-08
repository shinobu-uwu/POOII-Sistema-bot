class ComandoDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Comando já cadastrado")
