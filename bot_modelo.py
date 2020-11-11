from bot import Bot
import random
from comando_duplicado_exception import ComandoDuplicadoException


class BotModelo(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {"apresentacao" : [], "boas vindas" : [], "despedida" : []}

    @property
    def comandos(self):
        return self.__comandos
    
    def nome(self):
        return self.__nome

    def apresentacao(self):
        n = random.randrange(len(self.__comandos["apresentacao"]))
        return self.__comandos["apresentacao"][n]

    def mostra_comandos(self):
        resultado = ''
        for tipo in self.__comandos.values():
            for value in self.__comandos[tipo].values():
                resultado += value + "\n"
        return resultado

    def executa_comando(self, cmd):
        n = random.randrange(len(self.__comandos[cmd]))
        return self.__comandos[cmd][n]

    def boas_vindas(self):
        n = random.randrange(len(self.__comandos["boas vindas"]))
        return self.__comandos["boas vindas"][n]

    def despedida(self):
        n = random.randrange(len(self.__comandos["despedida"]))
        return self.__comandos["despedida"][n]

    def adiciona_comando(self, tipo, comando):
        if comando in self.__comandos[tipo]:
            raise ComandoDuplicadoException
        else:
            self.__comandos[tipo].append(comando)
        
    def remove_comando(self, tipo, comando):
        self.__comandos[tipo].remove(comando)
