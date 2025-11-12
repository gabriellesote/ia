# populacao.py
from individuo import Individuo

class Populacao:
    def __init__(self, tamanho_pop=None, tamanho_cromossomo=None, individuos=None):
        if individuos is not None:
            self.individuos = individuos
        else:
            self.individuos = [Individuo(tamanho=tamanho_cromossomo) for _ in range(tamanho_pop)]

    def get_individuos(self):
        return self.individuos
