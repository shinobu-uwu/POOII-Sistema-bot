import PySimpleGUI as sg


class AdicionarComandoView:
    def __init__(self, bot):
        self.__layout = [
            [sg.Text("Selecione um tipo de comando"), sg.Listbox([comando for comando in bot.comandos], size = (30, 3))],
            [sg.Button("Adicionar", key = "adicionar"), sg.Button("Cancelar", key = "cancelar")]
        ]
        self.__window = sg.Window("Adicionar comando", self.__layout, element_justification = "center")

    def le_eventos(self):
        return self.__window.read()
