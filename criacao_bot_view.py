import PySimpleGUI as sg


class CriacaoBotView:
    def __init__(self):
        self.__layout = [
            [sg.Text("Nome do bot"), sg.Input(key = "nome_bot")],
            [sg.Button("Adicionar bot", key = "adicionar_bot"), sg.Cancel(key = "cancelar")]
        ]
        self.__window = sg.Window("Criação de bot", self.__layout, element_justification = "center")

    def le_eventos(self):
        return self.__window.read()

    def atualiza_elemento(self, elemento, valor):
        self.__window.element(elemento).update(valor)

    def fecha(self):
        self.__window.close()
