# main.py
import sys
from mochila import Mochila
from algoritmo_genetico import AlgoritmoGenetico

def main():
    if len(sys.argv) < 7:
        print("Uso: python main.py <instancia> <pop> <taxaCruz> <taxaMut> <geracoes> <selecao>")
        print("Exemplo: python main.py instancias/inst1.txt 50 0.8 0.05 100 torneio")
        return

    caminho = sys.argv[1]
    pop = int(sys.argv[2])
    taxa_cruz = float(sys.argv[3])
    taxa_mut = float(sys.argv[4])
    geracoes = int(sys.argv[5])
    selecao = sys.argv[6]

    mochila = Mochila(caminho)
    ag = AlgoritmoGenetico(mochila, pop, taxa_cruz, taxa_mut, geracoes, selecao)
    melhor = ag.executar()

    print("\n📦 Melhor indivíduo encontrado:")
    print(f"Fitness: {melhor.get_fitness()}")
    print(f"Cromossomo: {melhor.get_cromossomo()}")

if __name__ == "__main__":
    main()
