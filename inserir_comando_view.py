import PySimpleGUI as sg


class InserirComandoView:
    def __init__(self, bot):
        self.__layout = [
            [sg.Text("Selecione um tipo de comando"), sg.Listbox([comando for comando in bot.comandos], size = (30, 3))],
            [sg.Button("Inserir", key = "inserir"), sg.Cancel()]
        ]
        self.__window = sg.Window("Inserir comando", self.__layout, element_justification = "center")

    def le_eventos(self):
        return self.__window.read()
