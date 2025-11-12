# mochila.py
from item import Item

class Mochila:
    def __init__(self, caminho_arquivo: str):
        self.capacidade = 0
        self.itens = []
        self._ler_arquivo(caminho_arquivo)

    def _ler_arquivo(self, caminho: str):
        with open(caminho, "r", encoding="utf-8") as f:
            self.capacidade = int(f.readline().strip())
            num_itens = int(f.readline().strip())

            for linha in f:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    nome = partes[0].strip()
                    peso = int(partes[1].strip())
                    valor = int(partes[2].strip())
                    self.itens.append(Item(nome, peso, valor))

        if len(self.itens) != num_itens:
            print("⚠️ Aviso: número de itens diferente do informado!")

    def get_capacidade(self):
        return self.capacidade

    def get_itens(self):
        return self.itens
