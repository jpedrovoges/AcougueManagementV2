class TelaCliente:

    def tela_opcoes(self):
        print('---- Cliente ----')
        print('Escolha a opção')
        print('1 - Cadastrar cliente')
        print('2 - Alterar cliente')
        print('3- Excluir cliente')
        print('4 - Listar clientes cadastrados')
        print('0 - Retornar')

        opcao = int(input('Escolha uma opção: '))
        return opcao

    def pega_dados(self):
        print("-------- DADOS CLIENTES ----------")
        nome = input('Nome: ')
        cpf = input('CPF: ')
        return {"nome": nome, "cpf": cpf}

    def lista_cliente(self, dados_clientes):
        string_cliente = ""
        for dado in dados_clientes:
            print(string_cliente + "NOME: " + dado["nome"])
            print(string_cliente + "CPF: " + str(dado["cpf"]) + '\n\n')

    def seleciona_cliente(self):
        cpf = input('Digite o cpf do cliente que deseja selecionar: ')
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
