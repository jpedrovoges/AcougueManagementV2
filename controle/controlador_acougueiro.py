from limite.tela_acougueiro import TelaAcougueiro
from entidade.acougueiro import Acougueiro
from DAOs.acougueiro_dao import AcougueiroDAO
from exceptions.JaExisteException import AcougueiroJaExisteException
from exceptions.ListaVaziaException import ListaVaziaException


class ControladorAcougueiro:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_acougueiro = TelaAcougueiro()
        self.__acougueiro_dao = AcougueiroDAO()

    def pega_acou_cpf(self, cpf: int):
        for acougueiro in self.__acougueiro_dao.get_all():
            if acougueiro.cpf == cpf:
                return acougueiro
        return None

    def lista_acougueiros(self):
        dados_acougueiro = []
        try:
            if len(self.__acougueiro_dao.get_all()) != 0:
                for acougueiro in self.__acougueiro_dao.get_all():
                    dados_acougueiro.append({"nome": acougueiro.nome, "cpf": acougueiro.cpf})
                self.__tela_acougueiro.lista_acoug(dados_acougueiro)
            else:
                raise ListaVaziaException
        except ListaVaziaException as e:
            self.__tela_acougueiro.mostra_mensagem(e)

    def contratar(self):
        dados = self.__tela_acougueiro.pega_dados()
        acoug = self.pega_acou_cpf(dados['cpf'])
        try:
            if acoug is None:
                acougueiro = Acougueiro(dados['nome'], dados['cpf'])
                self.__acougueiro_dao.add(acougueiro)
                self.__tela_acougueiro.mostra_mensagem('Açougueiro contratado!')

            else:
                raise AcougueiroJaExisteException
        except AcougueiroJaExisteException as e:
            self.__tela_acougueiro.mostra_mensagem(e)

    def alterar(self):
        self.lista_acougueiros()
        cpf = self.__tela_acougueiro.seleciona_acoug()
        acoug = self.pega_acou_cpf(cpf)

        if acoug is not None:
            novos_dados = self.__tela_acougueiro.pega_dados()
            acoug.nome = novos_dados["nome"]
            acoug.cpf = novos_dados["cpf"]
            self.__acougueiro_dao.update(acoug)
            self.lista_acougueiros()
        else:
            self.__tela_acougueiro.mostra_mensagem('Açougueiro não está no quadro de funcionários')

    def demitir(self):
        self.lista_acougueiros()
        cpf = self.__tela_acougueiro.seleciona_acoug()
        acoug = self.pega_acou_cpf(cpf)
        if acoug is not None:
            self.__acougueiro_dao.remove(acoug)
            self.__tela_acougueiro.mostra_mensagem('O açougueiro foi demitido')
            self.lista_acougueiros()

        else:
            self.__tela_acougueiro.mostra_mensagem('Açougueiro não consta em nosso quadro de funcionário.')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.contratar, 2: self.alterar,
                        3: self.demitir, 4: self.lista_acougueiros,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_acougueiro.tela_opcoes()]()
