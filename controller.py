from main_view import MainView
from cliente_dao import ClienteDAO
import PySimpleGUI as sg
from bot_modelo import BotModelo
from bot_duplicado_exception import BotDuplicadoException
from comando_duplicado_exception import ComandoDuplicadoException


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
                diretorio = sg.popup_get_file("Selecione o arquivo pkl do bot")
                try:
                    self.__cliente_dao.importar(diretorio)
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
                    diretorio = sg.popup_get_folder("Selecione onde deseja salvar o seu bot")
                    try:
                        assert diretorio is not None#Se o usuário clicar cancelar retorna None
                    except AssertionError:
                        pass #ignora e fecha a janela
                    else:
                        diretorio +=  f"/{bot.nome()}.pkl"
                        self.__cliente_dao.exportar(bot, diretorio)
                self.__atualiza_bots()
                
            elif event == "criar":
                try:
                   nome = sg.popup_get_text("Digite o nome do bot")
                   self.__cliente_dao.add(BotModelo(nome))
                except BotDuplicadoException:
                   sg.popup_error("Bot já cadastrado")
                self.__atualiza_bots()
                
            elif event == "remover":
                self.__cliente_dao.remove(values["lista_bots"][0])
                self.__atualiza_bots()
                    
    def __atualiza_bots(self):
        bots = [bot.nome() for bot in self.__cliente_dao.get_all()]
        self.__window.atualiza_elemento("lista_bots", bots)
        
