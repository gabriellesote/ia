# algoritmo_genetico.py

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import random
from populacao import Populacao
from individuo import Individuo


class AlgoritmoGenetico:
    def __init__(self, mochila, tamanho_pop, taxa_cruzamento, taxa_mutacao, geracoes, tipo_selecao,  tamanho_torneio=3):
        self.mochila = mochila
        self.tamanho_pop = tamanho_pop
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.geracoes = geracoes
        self.tipo_selecao = tipo_selecao
        self.tamanho_torneio = tamanho_torneio  # 👈 novo
        self.rand = random.Random()
        self.historico_fitness = []  # 📈 Armazena o melhor fitness de cada geração
        self.elitismo_ativo = True   # usado apenas para nomear o gráfico

    def executar(self, elitismo=True):
        self.elitismo_ativo = elitismo  # armazena o estado atual (para nomear o gráfico depois)

        tamanho_cromossomo = len(self.mochila.get_itens())
        pop = Populacao(self.tamanho_pop, tamanho_cromossomo)
        self._avaliar_populacao(pop)

        melhor = self._get_melhor_individuo(pop)

        for g in range(self.geracoes):
            nova_geracao = []

            # 🧬 Reprodução
            while len(nova_geracao) < self.tamanho_pop:
                pai1 = self._selecao(pop)
                pai2 = self._selecao(pop)
                filho = self._crossover(pai1, pai2)
                self._mutacao(filho)
                nova_geracao.append(filho)

            # 🧩 Elitismo opcional
            if elitismo:
                melhor_atual = self._get_melhor_individuo(pop)
                nova_geracao[0] = melhor_atual  # mantém o melhor indivíduo anterior

            # Atualiza população e avalia
            pop = Populacao(individuos=nova_geracao)
            self._avaliar_populacao(pop)

            melhor_geracao = self._get_melhor_individuo(pop)
            if melhor_geracao.get_fitness() > melhor.get_fitness():
                melhor = melhor_geracao

            self.historico_fitness.append(melhor.get_fitness())
            print(f"Geração {g+1:03d} | Melhor fitness: {melhor.get_fitness()}")

        # 🔥 Exibe e salva o gráfico após todas as gerações
        self._plotar_grafico()
        return melhor

    # Avaliação
    def _avaliar_populacao(self, pop):
        for ind in pop.get_individuos():
            ind.set_fitness(self._calcular_fitness(ind))

    def _calcular_fitness(self, ind):
        peso_total = 0
        valor_total = 0
        itens = self.mochila.get_itens()
        cromossomo = ind.get_cromossomo()

        for i, gene in enumerate(cromossomo):
            if gene == 1:
                peso_total += itens[i].peso
                valor_total += itens[i].valor

        # Penalização se ultrapassar capacidade
        if peso_total > self.mochila.get_capacidade():
            excesso = peso_total - self.mochila.get_capacidade()
            valor_total -= excesso * 10
            if valor_total < 0:
                valor_total = 0

        return valor_total

    # Seleção
    def _selecao(self, pop):
        if self.tipo_selecao.lower() == "torneio":
            return self._selecao_torneio(pop)
        else:
            return self._selecao_roleta(pop)

    def _selecao_torneio(self, pop):
        k = min(self.tamanho_torneio, len(pop.get_individuos()))  # 👈 usa o tamanho configurado
        competidores = random.sample(pop.get_individuos(), k)
        return max(competidores, key=lambda ind: ind.get_fitness())


    def _selecao_roleta(self, pop):
        soma_fitness = sum(ind.get_fitness() for ind in pop.get_individuos())
        if soma_fitness == 0:
            soma_fitness = 1

        ponto = random.uniform(0, soma_fitness)
        acumulado = 0
        for ind in pop.get_individuos():
            acumulado += ind.get_fitness()
            if acumulado >= ponto:
                return ind
        return pop.get_individuos()[-1]

    # Cruzamento e mutação
    def _crossover(self, pai1, pai2):
        c1 = pai1.get_cromossomo()
        c2 = pai2.get_cromossomo()

        if self.rand.random() < self.taxa_cruzamento:
            ponto_corte = self.rand.randint(0, len(c1) - 1)
            novo = [c1[i] if i < ponto_corte else c2[i] for i in range(len(c1))]
        else:
            novo = c1.copy()

        return Individuo(cromossomo=novo)

    def _mutacao(self, ind):
        cromossomo = ind.get_cromossomo()
        for i in range(len(cromossomo)):
            if self.rand.random() < self.taxa_mutacao:
                cromossomo[i] = 0 if cromossomo[i] == 1 else 1

    # Melhor indivíduo
    def _get_melhor_individuo(self, pop):
        return max(pop.get_individuos(), key=lambda ind: ind.get_fitness())

    # 📊 Plot e salvamento do gráfico de evolução
    def _plotar_grafico(self):
        plt.figure(figsize=(8, 5))
        plt.plot(self.historico_fitness, marker='o', linestyle='-', color='blue')
        plt.title("Evolução do Melhor Fitness por Geração")
        plt.xlabel("Geração")
        plt.ylabel("Melhor Fitness")
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()

        # 🔖 Nome do arquivo com base no tipo de execução
        tipo = "com_elitismo" if self.elitismo_ativo else "sem_elitismo"
        nome_arquivo = f"grafico_{tipo}.png"

        plt.savefig(nome_arquivo)
        print(f"📊 Gráfico salvo como '{nome_arquivo}'")
        plt.show()
