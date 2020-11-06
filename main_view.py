import PySimpleGUI as sg

class MainView:
    def __init__(self):
        self.__theme = sg.theme("DarkAmber")
        self.__layout = []
        self.__window = sg.Window('Sistema Chatbot', self.__layout)

    def mostra_view(self):
        self.__layout = [
                            [sg.Text("Olá, esse é o sistema de chatbots da empresa CrazyBots")],
                            [sg.Listbox([], key = "lista_bots", size = (30, 5))],
                            [sg.Button("Conversar", key = "conversa"), sg.Button("Importar", key = "import"), sg.Button("Exportar bot", key = "export"), sg.Button("Atualizar", key = "refresh")]
                        ]
        self.__window = sg.Window("Sistema Chatbot", self.__layout, element_justification = "center")
        return self.__layout

    def atualiza_elemento(self, elemento, valor):
        self.__window.Element(elemento).Update(valor)

    def le_eventos(self):
        return self.__window.Read()

    def fechar(self):
        self.__window.close()
