from bot_dao import BotDao
from main_view import View
from bot_view import BotView
from sistema_bot import SistemaChatBot, FabricaBot
import PySimpleGUI as sg

class Controller:
    def __init__(self):
        self.__window = View()
        self.__botWindow = BotView()
        self.__listaBots = FabricaBot().inicio()
        self.__bot_dao = BotDao()
        self.__sistema = SistemaChatBot("Crazy Bots")
        
    def comeca(self):
        window = self.__window
        rodando = True
        while rodando:
            window.mostra_view()
            event, values = window.le_eventos()
            print(event, values)
            bots = self.__bot_dao.get_all()
            nome_bots = ''
            for bot in bots:
                nome_bots += bot.nome()
            window.atualiza_elemento("lista_bots", nome_bots)
            if event ==  sg.WIN_CLOSED:
                rodando = False
            #elif event == "importar"

    def mostraWindow(self):
        self.__window = View()

    def mostraBotWindow(self):
        self.__botWindow = BotView()

    def atualizaWindow(self, elemento, valor):
        self.__window.update(elemento, valor)

    def fechaWindow(self):
        self.__window.fecha()

    def atualizaBotWindow(self, elemento, valor):
        self.__botWindow.update(elemento, valor)

    def fechaBotWindow(self):
        self.__botWindow.fecha()

    def exportarBot(self, bot):
        self.__bot_dao.exportar(bot)

    def importarBot(self, datasource):
        self.__bot_dao.importar(datasource)