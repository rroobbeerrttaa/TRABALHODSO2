from limite.tela_pessoa import TelaPessoa
from entidade.vendedor import Vendedor
from entidade.cliente import Cliente
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException


class ControladorPessoas():
    def __init__(self, controlador_sistema):
        self.__vendedores = []
        self.__clientes = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

        djonys = Vendedor('Djonys', "12345678901", "44445555", 100.00)
        ravi = Cliente('Ravi', "10987654321", "44332211")
        self.__vendedores.append(djonys)
        self.__clientes.append(ravi)

    @property
    def vendedores(self):
        return self.__vendedores
    
    @property
    def clientes(self):
        return self.__clientes

    def pega_cliente_por_cpf(self, cpf: str):
        for cliente in self.__clientes:
            if cliente.numero == cpf:
                return cliente
        return None

    def pega_vendedor_por_cpf(self, cpf: str):
        for vendedor in self.__vendedores:
            if vendedor.numero == cpf:
                return vendedor
        return None

    def incluir_cliente(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        try:
            if self.pega_cliente_por_cpf(dados_pessoa["cpf"]) is None:
                pessoa = Cliente(dados_pessoa["nome"],
                                dados_pessoa["cpf"],
                                dados_pessoa["celular"])
                self.__clientes.append(pessoa)
                self.__tela_pessoa.mostra_mensagem("Cliente incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)

    def incluir_vendedor(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        try:
            if self.pega_vendedor_por_cpf(dados_pessoa["cpf"]) is None:
                pessoa = Vendedor(dados_pessoa["nome"],
                                dados_pessoa["cpf"],
                                dados_pessoa["celular"], 
                                0)
                self.__vendedores.append(pessoa)
                self.__tela_pessoa.mostra_mensagem("Vendedor incluído com sucesso!")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)     

    def lista_cliente(self):
        if len(self.__clientes) == 0:
            self.__tela_pessoa.mostra_mensagem("Não há clientes cadastrados.")
            return None

        for cliente in self.__clientes:
            self.__tela_pessoa.mostra_cliente({"nome": cliente.nome,
                                               "cpf": cliente.numero,
                                               "celular": cliente.celular})

    def lista_vendedores(self):
        if len(self.__clientes) == 0:
            self.__tela_pessoa.mostra_mensagem("Não há vendedores cadastrados.")
            return None

        for vendedor in self.__vendedores:
            self.__tela_pessoa.mostra_vendedor({"nome": vendedor.nome,
                                                "cpf": vendedor.numero,
                                                "celular": vendedor.celular,
                                                "valor_vendido_total": vendedor.valor_vendido_total})

    def excluir_cliente(self):
        try:
            if len(self.__clientes) == 0:
                self.__tela_pessoa.mostra_mensagem("Não existe clientes para excluir")
            else:
                self.lista_cliente()
                cpf = self.__tela_pessoa.seleciona_pessoa()
                cliente = self.pega_cliente_por_cpf(cpf)
                if cliente is not None:
                    self.__clientes.remove(cliente)
                    self.__tela_pessoa.mostra_mensagem("Cliente excluído com sucesso!")
                    if len(self.__clientes) != 0:
                        self.__tela_pessoa.mostra_mensagem("Clientes restantes:")
                        self.lista_cliente()
                else:
                    raise NaoEncontradoNaListaException("cliente")
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)

    def excluir_vendedor(self):
        try:
            if len(self.__vendedores) == 0:
                self.__tela_pessoa.mostra_mensagem("Não existe vendedor para excluir")
            else:
                self.lista_vendedores()
                cpf = self.__tela_pessoa.seleciona_pessoa()
                vendedor = self.pega_vendedor_por_cpf(cpf)
                if vendedor is not None:
                    self.__vendedores.remove(vendedor)
                    self.__tela_pessoa.mostra_mensagem("Vendedor excluído com sucesso!")
                    if len(self.__vendedores) != 0:
                        self.__tela_pessoa.mostra_mensagem("Vendedores restantes:")
                        self.lista_vendedores()
                else:
                    raise NaoEncontradoNaListaException("vendedor")
        except Exception as e:
            self.__tela_pessoa.mostra_mensagem(e)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_cliente,
                        2: self.incluir_vendedor,
                        3: self.lista_cliente,
                        4: self.excluir_cliente,
                        5: self.lista_vendedores,
                        6: self.excluir_vendedor,
                        0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                lista_opcoes[opcao_escolhida]()
            else:
                self.__tela_pessoa.mostra_mensagem("Opção inválida, digite novamente.")