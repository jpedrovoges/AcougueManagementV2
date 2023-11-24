from limite.tela_entrega import TelaEntrega
from entidade.entrega import Entrega
from exceptions.JaExisteException import EntregaJaExisteException
from exceptions.ListaVaziaException import EntregaNaoExisteException
from DAOs.entrega_dao import EntregaDAO


class ControladorEntrega:
    def __init__(self, controlador_sistema):
        self.__tela_entrega = TelaEntrega(controlador_sistema)
        self.__controlador_sistema = controlador_sistema
        self.__entrega_dao = EntregaDAO()

    def entrega_por_cod(self, cod):
        for entrega in self.__entrega_dao.get_all():
            if entrega.cod == cod:
                return entrega
        return None

    def lista_entregas(self):
        dados_entregas = []
        try:
            if len(self.__entrega_dao.get_all()) != 0:
                for ent in self.__entrega_dao.get_all():
                    dados_entregas.append({'cod': ent.cod, 'cliente': ent.cliente.nome, 'carne': ent.estoque.corte})
                return self.__tela_entrega.mostra_entregas(dados_entregas)
            else:
                raise EntregaNaoExisteException
        except EntregaNaoExisteException as e:
            self.__tela_entrega.mostra_mensagem(e)

    def cria_entrega(self):
        self.__controlador_sistema.controlador_estoque.lista_carnes()
        dados_entrega = self.__tela_entrega.pega_dados()
        entreg = self.entrega_por_cod(dados_entrega["codigo"])
        try:
            cliente = self.__controlador_sistema.controlador_cliente.pega_cliente_cpf(dados_entrega["cpf"])
            if cliente is not None:
                if entreg is None:
                    carne = self.__controlador_sistema.controlador_estoque.pega_cod(dados_entrega['cod'])
                    entrega = Entrega(cliente, dados_entrega["codigo"], carne)
                    self.__entrega_dao.add(entrega)
                    self.__tela_entrega.mostra_mensagem("Sua entrega foi incluida!")
                else:
                    raise EntregaJaExisteException
            else:
                self.__tela_entrega.mostra_mensagem('Cliente não cadastrado, escolha um já existente')
                self.cria_entrega()
        except EntregaJaExisteException as e:
            self.__tela_entrega.mostra_mensagem('\n')
            self.__tela_entrega.mostra_mensagem(e)
            self.__tela_entrega.mostra_mensagem('\n')
            self.cria_entrega()

    def alterar_entrega(self):
        self.lista_entregas()
        cod = self.__tela_entrega.seleciona()
        entrega = self.entrega_por_cod(cod)
        if entrega is not None:
            novos_dados = self.__tela_entrega.pega_dados()
            entrega.cod = novos_dados["codigo"]
            entrega.cliente = novos_dados["cpf"]
            self.__entrega_dao.update(entrega)
            self.lista_entregas()
        else:
            self.__tela_entrega.mostra_mensagem('Codigo de entrega não corresponde a nenhuma entrega.')

    def excluir_entrega(self):
        self.lista_entregas()
        cod_entrega = self.__tela_entrega.seleciona()
        entrega = self.entrega_por_cod(cod_entrega)
        if entrega is not None:
            self.__entrega_dao.remove(entrega)
            self.__tela_entrega.mostra_mensagem('Entrega removida com sucesso')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_entrega, 2: self.alterar_entrega,
                        3: self.excluir_entrega, 4: self.lista_entregas,
                        0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_entrega.tela_opcoes()]()
