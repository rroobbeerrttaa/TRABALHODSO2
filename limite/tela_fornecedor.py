from teste.teste_numero_opcoes import TesteNumeroOpcoes
import math

class TelaFornecedor(TesteNumeroOpcoes):

    def __init__(self):
        pass

    def teste_do_cnpj(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 14:
                    return valor_recebido
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros e coloque 14 digitos. Exemplo 1234 (erro na digitação)")

    def teste_do_cep(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if len(valor_recebido) == 8:
                    return valor_recebido
                else:
                    raise ValueError
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros e com 8 digitos. Exemplo 1234 (erro na digitação)")
            
    def teste_do_float(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = float(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def teste_do_inteiro(self, mensagem=" "):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                return valor_recebido_tipo
            except ValueError:
                print("Por favor, escreva somente com numeros inteiros. Exemplo 1234 (erro na digitação)")

    def tela_opcoes(self):
        print("-------- FORNECEDOR ----------")
        print("1 - Incluir Fornecedor")
        print("2 - Alterar Fornecedor")
        print("3 - Listar Fornecedores")
        print("4 - Excluir Fornecedor")
        print("5 - Incluir Endereço")
        print("6 - Excluir Endereço")
        print("0 - Retornar")
    
        opcao = self.teste_numero_opcoes("Escolha a opção: ", [0,1,2,3,4,5,6])
        print("\n")
        return opcao

    def pega_dados_fornecedor(self):
        print("-------- DADOS FORNECEDOR ----------")
        nome = input("Nome/Razão Social: ")
        cnpj = self.teste_do_cnpj("CNPJ (sem pontos e coisas a mais): ")
        celular = self.teste_do_inteiro("Celular: ")
        produto = self.teste_do_inteiro("Código do produto: ")
        preco = self.teste_do_float("Preço: ")
        print("\n")
        return {
            "nome": nome,
            "cnpj": cnpj,
            "celular": celular,
            "produto": produto,
            "preco": preco
        }

    def mostra_fornecedor(self, dados_fornecedor):
        print("-------- DADOS DO FORNECEDOR ----------")
        print(f"Nome/Razão Social: {dados_fornecedor['nome']}")
        print(f"CNPJ: {dados_fornecedor['cnpj']}")
        print(f"Celular: {dados_fornecedor['celular']}")
        print(f"Produto: {dados_fornecedor['produto']}")
        print(f"Produto código: {dados_fornecedor['produto_codigo']}")
        print(f"Preço: R${float(dados_fornecedor['preco']):.2f}")
        
        if dados_fornecedor['enderecos']:
            print("Endereços:")
            for endereco in dados_fornecedor['enderecos']:
                print("- Rua: {}, Numero: {}, CEP:{}".format(endereco['rua'], endereco['numero'], endereco['cep']))
        else:
            print("Fornecedor sem endereços cadastrados.")
        print("\n")

    def pega_dados_endereco(self):
        print("-------- DADOS DO ENDEREÇO ----------")
        cep = self.teste_do_cep("CEP: ")
        rua = input("Rua: ")
        numero = self.teste_do_inteiro("Número: ")
        print("\n")
        return {"cep": cep, "rua": rua, "numero": numero}

    def seleciona_fornecedor(self):
        cnpj = self.teste_do_cnpj("Digite o CNPJ do fornecedor: ")
        print("\n")
        return cnpj

    def seleciona_endereco(self):
        cep = self.teste_do_cep("Digite o cep que deseja: ")
        print("\n")
        return cep

    def mostra_mensagem(self, msg):
        print(msg)
        print("\n")
