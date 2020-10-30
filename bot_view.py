import PySimpleGUI as sg

class BotView:
    def __init__(self):
        self.__layout = [
                            [sg.Text(key = "apresentação")],
                            [sg.Text(key = "comandos")]
                        ]
        self.__window = sg.Window("Converse com o bot!", self.__layout)

    def mostra_view(self):
        self.__window = sg.Window("Sistema Chatbot", self.__layout)
        return self.__layout

    def le_eventos(self):
        return self.__window.Read()

    def atualiza_elemento(self, elemento, valor):
        self.__window.Element(elemento).Update(valor)

    def fecha(self):
        self.__window.close