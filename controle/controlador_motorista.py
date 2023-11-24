from DAOs.motorista_dao import MotoristaDAO
from limite.tela_motorista import TelaMotorista
from entidade.motorista import Motorista
from exceptions.JaExisteException import MotoristaJaExisteException
from exceptions.ListaVaziaException import ListaVaziaException


class ControladorMotorista:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__motorista_dao = MotoristaDAO()
        self.__tela_motorista = TelaMotorista()

    def pega_motora_cpf(self, cpf: int):
        for motorista in self.__motorista_dao.get_all():
            if motorista.cpf == cpf:
                return motorista
        return None

    def lista_motoristas(self):
        dados_motorista = []
        try:
            if len(self.__motorista_dao.get_all()) != 0:
                for motorista in self.__motorista_dao.get_all():
                    dados_motorista.append({"nome": motorista.nome, "cpf": motorista.cpf})
                return self.__tela_motorista.mostra_mensagem(dados_motorista)
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_motorista.mostra_mensagem('\n')
            self.__tela_motorista.mostra_mensagem(e)
            self.__tela_motorista.mostra_mensagem('\n')

    def contratar(self):
        dados = self.__tela_motorista.pega_dados()
        motora = self.pega_motora_cpf(dados['cpf'])
        try:
            if motora is None:
                motorista = Motorista(dados['nome'], dados['cpf'])
                self.__motorista_dao.add(motorista)
                self.__tela_motorista.mostra_mensagem('Motorista contratado!')

            else:
                raise MotoristaJaExisteException
        except MotoristaJaExisteException as e:
            self.__tela_motorista.mostra_mensagem('\n')
            self.__tela_motorista.mostra_mensagem(e)
            self.__tela_motorista.mostra_mensagem('\n')

    def alterar(self):
        self.lista_motoristas()
        cpf = self.__tela_motorista.seleciona_motora()
        motora = self.pega_motora_cpf(cpf)

        if motora is not None:
            novos_dados = self.__tela_motorista.pega_dados()
            motora.nome = novos_dados["nome"]
            motora.cpf = novos_dados["cpf"]
            self.__motorista_dao.update(motora)
            self.lista_motoristas()
        else:
            self.__tela_motorista.mostra_mensagem('\n')
            self.__tela_motorista.mostra_mensagem('Motorista não está no quadro de funcionários')
            self.__tela_motorista.mostra_mensagem('\n')

    def demitir(self):
        self.lista_motoristas()
        cpf = self.__tela_motorista.seleciona_motora()
        motora = self.pega_motora_cpf(cpf)
        if motora is not None:
            self.__motorista_dao.remove(motora)
            self.__tela_motorista.mostra_mensagem('O motorista foi demitido')
            self.lista_motoristas()

        else:
            self.__tela_motorista.mostra_mensagem('Motorista não consta em nosso quadro de funcionário.')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.contratar, 2: self.alterar,
                        3: self.demitir, 4: self.lista_motoristas,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_motorista.tela_opcoes()]()
