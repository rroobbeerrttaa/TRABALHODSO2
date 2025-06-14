from abc import ABC, abstractmethod

class TesteNumeroOpcoes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def teste_numero_opcoes(self, mensagem=" ", valores_validos = None):
        while True:
            valor_recebido = input(mensagem)
            try:
                valor_recebido_tipo = int(valor_recebido)
                if valores_validos and valor_recebido_tipo not in valores_validos:
                    raise ValueError
                return valor_recebido_tipo
            except ValueError:
                print("Você não digitou um valor aceitavel, digite novamente")
                print("Esses são os valores aceitáveis:", valores_validos)
                print("\n")
    