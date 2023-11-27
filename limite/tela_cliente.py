import PySimpleGUI as sg


class TelaCliente:
    def __init__(self):
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
        sg.ChangeLookAndFeel('DarkGray2')
        layout = [
            [sg.Text('Escolha sua opção', font=("TimesNewRoman", 15))],
            [sg.Radio('Incluir cliente', "RD1", key='1')],
            [sg.Radio('Alterar dados do cliente', "RD1", key='2')],
            [sg.Radio('Excluir cliente', "RD1", key='3')],
            [sg.Radio('Listar clientes', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cliente').Layout(layout)

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Dados Cliente', font=("TimesNewRoman", 20))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Estoque').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        cpf = values['cpf']

        self.close()
        return {'nome': nome, "cpf": cpf}

    def lista_clientes(self, dados_clientes):
        string_cliente = ""
        for dado in dados_clientes:
            string_cliente = string_cliente + "Nome:" + dado["nome"] + '\n'
            string_cliente = string_cliente + "CPF: " + str(dado["cpf"]) + '\n\n'

        sg.Popup('Clientes', string_cliente)

    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Digite o cpf do cliente que deseja alterar', font=("TimesNewRoman", 25))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Selecionar CPF do cliente').Layout(layout)
        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values
