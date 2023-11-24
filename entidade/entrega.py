from entidade.cliente import Cliente
from entidade.estoque import Estoque


class Entrega:
    def __init__(self, cliente: Cliente, cod: int, estoque: Estoque):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(estoque, Estoque):
            self.__estoque = estoque
        self.__cod = cod

    @property
    def estoque(self):
        return self.__estoque

    @estoque.setter
    def estoque(self, estoque):
        if isinstance(estoque, Estoque):
            self.__estoque = estoque

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod):
        self.__cod = cod
