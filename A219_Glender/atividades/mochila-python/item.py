# item.py
class Item:
    def __init__(self, nome: str, peso: int, valor: int):
        self.nome = nome
        self.peso = peso
        self.valor = valor

    def __repr__(self):
        return f"{self.nome}(peso={self.peso}, valor={self.valor})"
