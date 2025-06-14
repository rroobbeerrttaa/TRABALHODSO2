class TelaSistema:
    def teste_numero_opcoes(self, mensagem = " ", valores_validos = None):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if valores_validos and valor_recebido_tipo not in valores_validos:
                    raise ValueError
                return valor_recebido_tipo
            except ValueError:
                print("Opção inválida, digite novamente")

    def tela_opcoes(self):
        print("========== SISTEMA DE ESTOQUE DA A5 ==========")
        print()
        print("1 - Venda feita pelo Vendedor")
        print("2 - Fornecedor")
        print("3 - Produto")
        print("4 - Pessoa")
        print("5 - Pedido feito para o fornecedor")
        print("6 - Relatórios")
        print("0 - Finalizar sistema")
        print()
        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6])
        print()
        return opcao
    
    def mostra_mensagem(self, msg: str):
        print(msg)
        print()
