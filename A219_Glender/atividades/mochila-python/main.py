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

# 👇 se não passar, padrão = 3
    if len(sys.argv) >= 8:
        tamanho_torneio = int(sys.argv[7])
    else:
        tamanho_torneio = 3
        
        
    mochila = Mochila(caminho)

    # 🧬 Teste com ELITISMO
    print("\n==============================")
    print("🚀 TESTE COM ELITISMO")
    print("==============================")
    ag_com = AlgoritmoGenetico(
        mochila, pop, taxa_cruz, taxa_mut, geracoes, selecao)
    melhor_com = ag_com.executar(elitismo=True)
    print("\n📦 Melhor indivíduo (com elitismo):")
    print(f"Fitness: {melhor_com.get_fitness()}")
    print(f"Cromossomo: {melhor_com.get_cromossomo()}")

    # 🧬 Teste SEM ELITISMO
    print("\n==============================")
    print("⚙️ TESTE SEM ELITISMO")
    print("==============================")
    ag_sem = AlgoritmoGenetico(
        mochila, pop, taxa_cruz, taxa_mut, geracoes, selecao)
    melhor_sem = ag_sem.executar(elitismo=False)
    print("\n📦 Melhor indivíduo (sem elitismo):")
    print(f"Fitness: {melhor_sem.get_fitness()}")
    print(f"Cromossomo: {melhor_sem.get_cromossomo()}")

    # ✅ Comparação final
    print("\n==============================")
    print("📊 COMPARAÇÃO FINAL")
    print("==============================")
    print(f"Com elitismo  -> Fitness: {melhor_com.get_fitness()}")
    print(f"Sem elitismo  -> Fitness: {melhor_sem.get_fitness()}")


if __name__ == "__main__":
    main()
