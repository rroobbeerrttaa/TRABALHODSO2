from datetime import datetime
from teste.teste_numero_opcoes import TesteNumeroOpcoes


class TelaPedido(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_cnpj(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 14:
                    return valor_recebido_tipo
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros e coloque 14 digitos. Exemplo 1234 (erro na digitação)")

    def teste_do_float(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = float(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros. Exemplo 12.55 (erro na digitação)")

    def teste_do_inteiro(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def teste_da_data(self, mensagem=" "):
        while True:
            try:
                data = input(mensagem)
                data_recebida = datetime.strptime(data, "%d/%m/%Y")  
                return data_recebida
            except ValueError:
                print("Data inválida. Insira a data no formato (dd/mm/yyyy) (erro na digitacao).")

    def tela_opcoes(self):
        print("-------- PEDIDOS ----------")
        print("Escolha a opcao")
        print("1 - Fazer Pedido")
        print("2 - Listar Pedido")
        print("3 - Excluir Pedido")
        print("4 - Alterar Pedido")
        print("0 - Retornar")

        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0,1,2,3,4])
        print("\n")
        return opcao

    def pega_dados_pedido(self):
        print("-------- DADOS PEDIDOS ----------")
        cnpj = self.teste_do_cnpj("CNPJ do fornecedor: ")
        codigo = self.teste_do_inteiro("Codigo do pedido: ")
        codigo_produto = self.teste_do_inteiro("Codigo do Produto: ")
        quantidade = self.teste_do_inteiro("Quantidade do pedido: ")
        data = self.teste_da_data("Data do pedido feito (DD/MM/AAAA): ")
        valor_frete = self.teste_do_float("Valor do frete do pedido: ")
        prazo_entrega = self.teste_do_inteiro("Prazo do pedido (quantidade de dias): ")

        return {"cnpj": cnpj, "codigo": codigo,
                "codigo_produto": codigo_produto,
                "quantidade": quantidade,
                "data": data,
                "valor_frete": valor_frete,
                "prazo_entrega": prazo_entrega}
    
    def altera_dados_pedidos(self):
        print("-------- NOVOS DADOS PEDIDOS ----------")
        cnpj = self.teste_do_cnpj("CNPJ do fornecedor: ")
        codigo_produto = self.teste_do_inteiro("Codigo do Produto: ")
        quantidade = self.teste_do_inteiro("Quantidade do pedido: ")
        data = self.teste_da_data("Data do pedido feito (DD/MM/AAAA): ")
        valor_frete = self.teste_do_float("Valor do frete do pedido: ")
        prazo_entrega = self.teste_do_inteiro("Prazo do pedido (quantidade de dias): ")

        return {"cnpj": cnpj,
                "codigo_produto": codigo_produto,
                "quantidade": quantidade,
                "data": data,
                "valor_frete": valor_frete,
                "prazo_entrega": prazo_entrega}
    

    def mostra_pedidos(self, dados_pedidos):
        print("CODIGO DO PEDIDO: ", dados_pedidos["codigo"])
        print("QUANTIDADE DO PEDIDO: ", dados_pedidos["quantidade"])
        print("NOME DO PRODUTO: ", dados_pedidos["nome_produto"])
        print("DATA DO PEDIDO: ", dados_pedidos["data"])
        print("VALOR DO PRODUTO: ", dados_pedidos["valor"])
        print("NOME DO FORNECEDOR: ", dados_pedidos["nome_fornecedor"])
        print("VALOR DO FRETE: ", dados_pedidos["frete"])
        print("PRAZO DE ENTREGA: ", dados_pedidos["prazo_entrega"])
        print("\n")

    def seleciona_pedido(self):
        codigo = self.teste_do_inteiro("Código do pedido que deseja selecionar: ")
        return codigo
    
    def mostra_mensagem(self, msg):
        print(msg)