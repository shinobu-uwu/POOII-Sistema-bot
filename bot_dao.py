import pickle
from bot import Bot

class BotDao:
    def __init__(self, datasource = "bot.pkl"):
        self.__datasource = datasource
        self.__object_cache = {}

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
            self.__object_cache[bot.nome()] = bot
            self.__dump()

    def get(self, nome):
        return self.__object_cache[nome]

    def remove(self, nome):
        self.__object_cache.pop(nome)

    def get_all(self):
        return list(self.__object_cache.values())

    def importar(self, datasource):
        try:
            file = open(self.__datasource, 'rb')
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            a = pickle.load(file)
            self.__object_cache[a.nome()] = a

    def exportar(self, bot, datasource= "export.pkl"):
        file = open(datasource, 'wb')
        pickle.dump(bot, file)
