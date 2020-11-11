from main_view import MainView
from cliente_dao import ClienteDAO
import PySimpleGUI as sg
from bot_modelo import BotModelo
from bot_duplicado_exception import BotDuplicadoException
from comando_duplicado_exception import ComandoDuplicadoException
from criacao_bot_view import CriacaoBotView
from inserir_comando_view import InserirComandoView


class Controller:
    def __init__(self):
        self.__window = MainView()
        self.__cliente_dao = ClienteDAO()

    def comeca(self):
        bots = [bot.nome() for bot in self.__cliente_dao.get_all()]
        self.__window.mostra_view(bots)
        rodando = True
        while rodando:
            event, values = self.__window.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
                
            elif event == "refresh":
                self.__atualiza_bots()
                
            elif event == "importar":
                try:
                    diretorio = sg.popup_get_file("Selecione o arquivo pkl do bot")
                    assert diretorio is not None
                    self.__cliente_dao.importar(diretorio)
                #Se o usuário clicar em cancelar o diretório é None
                except AssertionError:
                    pass #Ignora e fecha a janela
                except BotDuplicadoException:
                    sg.popup_error("Bot já cadastrado no sistema")
                self.__atualiza_bots()
                
            elif event == "exportar":
                try:
                    #listbox retorna uma lista com os itens selecionados, por enquanto só funciona com um bot
                    bot = self.__cliente_dao.get(values["lista_bots"][0])
                except IndexError:
                    sg.popup_error("Selecione um bot")
                else:
                    #essa função só pega o diretório, então adiciono o nome do bot e a extensão pra exportar, por enquanto o usuário não pode escolher o nome do arquivo
                    try:
                        diretorio = sg.popup_get_folder("Selecione onde deseja salvar o seu bot")
                        assert diretorio is not None#Se o usuário clicar cancelar retorna None
                    except AssertionError:
                        pass
                    else:
                        diretorio +=  f"/{bot.nome()}.pkl"
                        self.__cliente_dao.exportar(bot, diretorio)
                self.__atualiza_bots()
                
            elif event == "criar":
                self.criar_bot()
                
            elif event == "remover":
                try:
                    self.__cliente_dao.remove(values["lista_bots"][0])
                except IndexError:
                    sg.popup_error("Selecione um bot")
                finally:
                    self.__atualiza_bots()

            elif event == "adicionar_comando":
                try:
                    bot = self.__cliente_dao.get(values["lista_bots"][0])
                except IndexError:
                    sg.popup_error("Selecione um bot")
                else:
                    self.adicionar_comando(bot)
                
    def __atualiza_bots(self):
        bots = [bot.nome() for bot in self.__cliente_dao.get_all()]
        self.__window.atualiza_elemento("lista_bots", bots)
        
    def criar_bot(self):
        window = CriacaoBotView()
        rodando = True
        while rodando:
            event, values = window.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "adicionar_bot":
                bot = BotModelo(values["nome_bot"])
                try:
                    self.__cliente_dao.add(bot)
                except BotDuplicadoException:
                    sg.popup_error("Bot já cadastrado no sistema")
                else:
                    window.fecha()
                    self.__atualiza_bots()

            elif event == "cancelar":
                window.fecha()

    def adicionar_comando(self, bot):
        window = InserirComandoView(bot)
        rodando = True
        while rodando:
            event, values = window.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False

            elif event == "inserir":
                try:
                    bot.adiciona_comando(values["comandos"][0], values["comando"])
                    self.__cliente_dao.remove(bot.nome())
                    self.__cliente_dao.add(bot)
                except IndexError:
                    sg.popup_error("Selecione um tipo de comando")
                except ComandoDuplicadoException:
                    sg.popup_error("Comando já existente no bot")
                else:
                    self.__atualiza_bots()
                    window.fecha()
                    
            elif event == "cancelar":
                window.fecha()
