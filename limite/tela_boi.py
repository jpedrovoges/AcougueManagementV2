import PySimpleGUI as sg


class TelaBoi:
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
            [sg.Radio('Incluir boi', "RD1", key='1')],
            [sg.Radio('Alterar dados do boi', "RD1", key='2')],
            [sg.Radio('Excluir boi', "RD1", key='3')],
            [sg.Radio('Listar bois', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Boi').Layout(layout)

    def pega_dados(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Dados boi', font=("TimesNewRoman", 20))],
            [sg.Text('Número do boi:', size=(15, 1)), sg.InputText('', key='num')],
            [sg.Spin(values=('Dianteiro', 'Traseiro'), initial_value='selecione', key='parte')],
            [sg.Text('Peso:', size=(15, 1)), sg.InputText('', key='peso')],
            [sg.Button('Confirmar')]
        ]
        self.__window = sg.Window('Estoque').Layout(layout)

        button, values = self.open()
        num = values['num']
        parte = values['parte']
        peso = values['peso']

        self.close()
        return {'num': num, "parte": parte, "peso": peso}

    def lista_bois(self, dados_bois):
        string_boi = ""
        for dado in dados_bois:
            string_boi = string_boi + "Número do boi:" + str(dado["num"]) + '\n'
            string_boi = string_boi + "Parte:" + dado["parte"] + '\n'
            string_boi = string_boi + "Peso: " + str(dado["peso"]) + '\n\n'

        sg.Popup('Bois', string_boi)

    def seleciona_boi(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
            [sg.Text('Digite o número do boi que deseja alterar', font=("TimesNewRoman", 25))],
            [sg.Text('Número do boi:', size=(15, 1)), sg.InputText('', key='num')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]
        self.__window = sg.Window('Selecionar o número do boi').Layout(layout)
        button, values = self.open()
        num = values['num']
        self.close()
        return num

    def mostra_mensagem(self, msg):
        sg.popup("", msg)

    def open(self):
        button, values = self.__window.Read()
        return button, values