import PySimpleGui as sg

class View:
    def __init__(self):
        self.__layout = []
        self.__window = sg.Window('Sistema Chatbot', self.__layout)

    def mostra_view(self):
        self.__layout = [
                            [sg.Text(size = (10, 1)), sg.Text("Olá, esse é o sistema de chatbots da empresa CrazyBots"), sg.Text(size = (10, 1))],
                            [sg.Combo(key = "lista_bots", readonly = True)],
                            [sg.Button("Conversar com o bot", key = "conversa"), sg.Button("Importar bot", key = "import"), sg.Button("Exportar bot", key = "export")]
                        ]
        self.__window = sg.Window("Sistema Chatbot", self.__layout)
        return self.__layout

    def atualiza_elemento(self, elemento, valor):
        self.__window.Element(elemento).Update(valor)

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()
