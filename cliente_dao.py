import pickle
from bot import Bot
from bot_duplicado_exception import BotDuplicadoException


class ClienteDAO:
    def __init__(self, datasource = "bot.pkl"):
        self.__datasource = datasource
        self.__object_cache = {}
        self.__load()
        
    @property
    def object_cache(self):
        return self.__object_cache

    def __dump(self):
        file = open(self.__datasource, 'wb')
        pickle.dump(self.__object_cache, file)

    def __load(self):
        try:
            file = open(self.__datasource, "rb")
        except FileNotFoundError:
            self.__dump()
            self.__load()
        else:
            self.__object_cache = pickle.load(file)
        
    def add(self, bot):
        if isinstance(bot, Bot):
            if bot.nome() not in self.__object_cache:
                self.__object_cache[bot.nome()] = bot
                self.__dump()
            else:
                raise BotDuplicadoException

    def get(self, nome):
        return self.__object_cache[nome]

    def remove(self, nome):
        self.__object_cache.pop(nome)

    def get_all(self):
        return list(self.__object_cache.values())

    def importar(self, datasource):
        file = open(datasource, "rb")
        objeto = pickle.load(file)
        self.add(objeto)

    def exportar(self, bot, datasource= "export.pkl"):
        file = open(datasource, 'wb')
        pickle.dump(bot, file)
