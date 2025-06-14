from limite.tela_pedido import TelaPedido
from entidade.pedido import Pedido
from excessoes.encontrado_na_lista_exception import EncontradoNaListaException
from excessoes.nao_encontrado_na_lista_exception import NaoEncontradoNaListaException

class ControladorPedidos():
    def __init__(self, controlador_sistema):
        self.__pedidos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_pedido = TelaPedido()

    def pega_pedido_por_codigo(self, codigo: int):
        for i in self.__pedidos:
            if i.codigo == codigo:
                return i
        return None

    def incluir_pedido(self):
        self.__controlador_sistema.controlador_fornecedores.lista_fornecedores()
        self.__controlador_sistema.controlador_produtos.lista_produtos()

        dados_pedido = self.__tela_pedido.pega_dados_pedido()
        codigo_pedido = self.pega_pedido_por_codigo(dados_pedido["codigo"])
        try:
            if codigo_pedido is None:
                objeto_fornecedor = self.__controlador_sistema.controlador_fornecedores.pega_fornecedor_por_cnpj(dados_pedido["cnpj"])
                if objeto_fornecedor is not None:
                    objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(dados_pedido["codigo_produto"])
                    if int(objeto_fornecedor.produto.codigo_produto) == int(dados_pedido["codigo_produto"]):
                        valor = (float(dados_pedido["quantidade"]) * float(objeto_fornecedor.preco) + float(dados_pedido["valor_frete"]))
                        pedido = Pedido(int(dados_pedido["quantidade"]),
                                        objeto_produto,
                                        dados_pedido["data"],
                                        valor,
                                        dados_pedido["codigo"],
                                        objeto_fornecedor,
                                        dados_pedido["valor_frete"],
                                        dados_pedido["prazo_entrega"])
                        self.__pedidos.append(pedido)   
                        objeto_produto.quant_estoque = int(objeto_produto.quant_estoque) + int(dados_pedido["quantidade"])
                        self.__tela_pedido.mostra_mensagem("Adicionado com sucesso!")

                    else:
                        raise NaoEncontradoNaListaException("produto")
                else:
                    raise NaoEncontradoNaListaException("fornecedor")
            else:
                raise EncontradoNaListaException()
        except Exception as e:
            self.__tela_pedido.mostra_mensagem(e)

    def alterar_pedido(self):
        self.lista_pedidos()
        codigo_pedido = self.__tela_pedido.seleciona_pedido()
        pedido = self.pega_pedido_por_codigo(codigo_pedido)
        try:
            if pedido is not None:
                self.__controlador_sistema.controlador_fornecedores.lista_fornecedores()
                self.__controlador_sistema.controlador_produtos.lista_produtos()
                novos_dados = self.__tela_pedido.altera_dados_pedidos()
                novo_fornecedor = self.__controlador_sistema.controlador_fornecedores.pega_fornecedor_por_cnpj(novos_dados["cnpj"])
                if novo_fornecedor is not None:
                    novo_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(novos_dados["codigo_produto"])
                    if (novo_produto is not None) and (novo_produto.codigo_produto == novo_fornecedor.produto.codigo_produto):
                        produto_antigo = pedido.produto
                        produto_antigo.quant_estoque -= pedido.quantidade
                        novo_valor = (float(novos_dados["quantidade"]) * float(novo_fornecedor.preco) + float(novos_dados["valor_frete"]))
            
                        pedido.quantidade = int(novos_dados["quantidade"])
                        pedido.produto = novo_produto
                        pedido.data = novos_dados["data"]
                        pedido.valor = novo_valor
                        pedido.fornecedor = novo_fornecedor
                        pedido.frete = float(novos_dados["valor_frete"])
                        pedido.prazo_entrega = int(novos_dados["prazo_entrega"])
                        
                        novo_produto.quant_estoque += int(novos_dados["quantidade"])
                        
                        self.__tela_pedido.mostra_mensagem("Pedido alterado com sucesso!")
                    else:
                        raise NaoEncontradoNaListaException("produto")
                else:
                    raise NaoEncontradoNaListaException("fornecedor")
            else:
                raise NaoEncontradoNaListaException("pedido")
            
        except Exception as e:
            self.__tela_pedido.mostra_mensagem(e)

    def lista_pedidos(self):
        if len(self.__pedidos) != 0:
            for pedido in self.__pedidos:
                pedido = ({"codigo": pedido.codigo,
                        "quantidade": pedido.quantidade,
                        "nome_produto": pedido.produto.nome,
                        "data": pedido.data,
                        "valor": pedido.valor,
                        "nome_fornecedor": pedido.fornecedor.nome, 
                        "frete": pedido.frete,
                        "prazo_entrega": pedido.prazo_entrega})
                self.__tela_pedido.mostra_pedidos(pedido)
        else:
            self.__tela_pedido.mostra_mensagem("Não exite pedidos feitos!")

    def excluir_pedido(self):
        if len(self.__pedidos) != 0:
            self.lista_pedidos()
            codigo_pedido = self.__tela_pedido.seleciona_pedido()
            pedido = self.pega_pedido_por_codigo(codigo_pedido)
            try:
                if pedido is not None:
                    objeto_produto = self.__controlador_sistema.controlador_produtos.pega_produto_por_codigo(pedido.produto.codigo_produto)
                    objeto_produto.quant_estoque = int(objeto_produto.quant_estoque) - int(pedido.quantidade)
                    self.__pedidos.remove(pedido)
                    self.__tela_pedido.mostra_mensagem("Removido com sucesso!")
                else:
                    raise NaoEncontradoNaListaException("pedido")
            except Exception as e:
                self.__tela_pedido.mostra_mensagem(e)
        else:
            self.__tela_pedido.mostra_mensagem("Não exite pedidos para remover!")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pedido,
                        2: self.lista_pedidos,
                        3: self.excluir_pedido,
                        4: self.alterar_pedido,
                        0: self.retornar}

        continua = True
        while continua:
            opcao = self.__tela_pedido.tela_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
