import PySimpleGUI as sg


class TelaEntrega:

    def __init__(self, controlador_sistema):
        self.__cliente = controlador_sistema.controlador_cliente
        self.__estoque = controlador_sistema.controlador_estoque
        self.__window = None
        self.init_components()

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

    def close(self):
        self.__window.Close()

    def init_components(self):
        # sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkGray2')
        layout = [
            [sg.Text('Escolha sua opção', font=("TimesNewRoman", 15))],
            [sg.Radio('Criar entrega', "RD1", key='1')],
            [sg.Radio('Alterar entrega', "RD1", key='2')],
            [sg.Radio('Excluir entrega', "RD1", key='3')],
            [sg.Radio('Listar entregas', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Entrega').Layout(layout)

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Dados Entrega', font=("TimesNewRoman", 20))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Entrega').Layout(layout)

        button, values = self.open()
        codigo = values['cod']
        cpf = values['cpf']

        self.close()
        return {"cpf": cpf, "cod": codigo}

    def mostra_entregas(self, dados_entregas):
        string_entrega = ""
        for dado in dados_entregas:
            string_entrega = string_entrega + "Cod: " + dado["cod"] + '\n'
            string_entrega = string_entrega + "Cliente: " + dado["cliente"] + '\n\n'

        sg.Popup('Entrega', string_entrega)

    def adc_carne(self):
        self.__estoque.lista_carnes()
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Digite o codigo da carne', font=("TimesNewT=Roman", 20))],
            [sg.Text('Código:', size=(15,1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar')]]
        self.__window = sg.Window('Adiciona carne').Layout(layout)
        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod

    def seleciona(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Digite o cod da entrega que deseja alterar', font=("TimesNewRoman", 20))],
            [sg.Text('Código:', size=(15,1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar')]]
        self.__window = sg.Window('Seleciona cod da carne').Layout(layout)
        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values