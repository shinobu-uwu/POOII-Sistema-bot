class BotDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Bot já cadastrado no sistema")
