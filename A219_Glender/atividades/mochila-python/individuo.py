# individuo.py
import random

class Individuo:
    def __init__(self, tamanho=None, cromossomo=None):
        if cromossomo is not None:
            self.cromossomo = cromossomo.copy()
        else:
            self.cromossomo = [random.choice([0, 1]) for _ in range(tamanho)]
        self.fitness = 0

    def get_cromossomo(self):
        return self.cromossomo

    def set_fitness(self, valor):
        self.fitness = valor

    def get_fitness(self):
        return self.fitness

    def __repr__(self):
        return f"Individuo(fitness={self.fitness}, cromossomo={self.cromossomo})"
