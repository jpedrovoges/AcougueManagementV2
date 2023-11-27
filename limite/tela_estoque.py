import PySimpleGUI as sg


class TelaEstoque:
    def __init__(self):
        self.__window = None
        self.init_components()

    def close(self):
        self.__window.Close()

    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray2')
        layout = [
            [sg.Text('Escolha sua opção', font=("TimesNewRoman", 15))],
            [sg.Radio('Incluir corte', "RD1", key='1')],
            [sg.Radio('Alterar corte', "RD1", key='2')],
            [sg.Radio('Excluir corte', "RD1", key='3')],
            [sg.Radio('Listar estoque', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Estoque').Layout(layout)

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Dados Carne', font=("TimesNewRoman", 20))],
            [sg.Text('Codigo:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Text('Corte:', size=(15, 1)), sg.InputText('', key='corte')],
            [sg.Text('Qtd:', size=(15, 1)), sg.InputText('', key='qtd')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Estoque').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        corte = values['corte']
        qtd = values['qtd']

        self.close()
        return {"cod": cod, "corte": corte, "qtd": qtd}

    def seleciona(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Digite o cod do corte que deseja alterar', font=("TimesNewRoman", 25))],
            [sg.Text('Cod:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Seleciona cod da carne').Layout(layout)
        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod

    def lista_carnes(self, dados_carne):
        string_carne = ""
        for dado in dados_carne:
            string_carne = string_carne + "Código:" + dado["cod"] + '\n'
            string_carne = string_carne + "Corte:" + str(dado["corte"]) + '\n'
            string_carne = string_carne + "Quantidade: " + str(dado["qtd"]) + '\n\n'

        sg.Popup('Estoque', string_carne)

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values
