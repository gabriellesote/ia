# 📦 Algoritmo Genético – Problema da Mochila

#### Trabalho Prático – Inteligência Artificial

Este projeto implementa um Algoritmo Genético (AG) para resolver o Problema da Mochila 0/1, utilizando seleção por torneio ou roleta, crossover, mutação, elitismo opcional e visualização gráfica da evolução do fitness.

O código foi totalmente estruturado em Python, com arquivos separados para organização e leitura de instâncias via arquivo .txt.

### 🧰 1. Requisitos
✔ Python 3.10+
✔ Virtualenv (recomendado)
✔ Matplotlib (para gráficos)



### 🏗️ 2. Instalação

Recomenda-se usar um ambiente virtual

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Instalar dependências:

```
pip install matplotlib
```

### 📁 3. Estrutura do Projeto

```
mochila-python/
│
├── algoritmo_genetico.py   # Implementação principal do AG
├── individuo.py            # Representação do indivíduo (cromossomo)
├── populacao.py            # Representação da população
├── mochila.py              # Leitura e armazenamento da instância
├── main.py                 # Arquivo principal de execução
│
└── instancias/
      └── inst1.txt         # Exemplo de instância do problema

```


### 🧪 4. Como Executar
A execução segue o formato:

```
python main.py <instancia> <pop> <taxaCruz> <taxaMut> <geracoes> <selecao> [tamanho_torneio]
```

```
python main.py instancias/inst1.txt 10 0.7 0.03 15 torneio 5
```

```
python main.py instancias/inst1.txt 10 0.7 0.03 15 roleta
```

### ⚙️ 5. Parâmetros

| Parâmetro         | Descrição                                     |
| ----------------- | --------------------------------------------- |
| `instancia`       | Caminho do arquivo com os itens (peso, valor) |
| `pop`             | Tamanho da população                          |
| `taxaCruz`        | Probabilidade de crossover                    |
| `taxaMut`         | Probabilidade de mutação                      |
| `geracoes`        | Número total de gerações                      |
| `selecao`         | `"torneio"` ou `"roleta"`                     |
| `tamanho_torneio` | (Opcional) Define k no torneio                |

### 📄 6. Formato das Instâncias

Uma instância .txt segue este formato:

```
50
10
Notebook, 15, 40
Celular, 10, 30
Câmera, 20, 60
Livro, 5, 10
Carregador, 2, 8
```
 - Linha 1: capacidade da mochila
 - Linha 2: quantidade de itens
 - Demais: nome, peso, valor

### 🧬 7. Como o código funciona
#### 🔸 Individuo (individuo.py)

Representa uma solução do AG, contendo:
Cromossomo binário (lista de 0 e 1)
Método para armazenar fitness

#### 🔸 População (populacao.py)

Conjunto de vários indivíduos.
Permite criar populações iniciais ou substituir por uma nova geração.

#### 🔸 Mochila (mochila.py)

Responsável por:
- Ler o arquivo .txt
- Guardar capacidade
- Guardar lista de itens (peso e valor)

#### 🔸 Algoritmo Genético (algoritmo_genetico.py)

Implementa as etapas do AG:

✔ Avaliação (fitness)

- Soma valores dos itens selecionados
- Penaliza excesso de peso:
    fitness -= excesso * 10

✔ Seleção

- Torneio: melhor entre k competidores
- Roleta: probabilidade proporcional ao fitness

✔ Crossover

1-ponto (com probabilidade definida)

✔ Mutação

Troca bits de 0↔1 conforme taxa de mutação

✔ Elitismo

Opcional: preserva o melhor indivíduo de cada geração.

✔ Gráfico

Gera arquivo grafico_*.png mostrando a evolução do fitness.

#### 🔸 Main (main.py)

Controla toda a execução:

Lê parâmetros do terminal

Cria objetos necessários

Executa o AG com ou sem elitismo

Exibe melhor indivíduo

Salva gráficos de desempenho


### 📊 8. Exemplo de Saída

```
Geração 001 | Melhor fitness: 142
Geração 002 | Melhor fitness: 150
Geração 003 | Melhor fitness: 150
...
📦 Melhor indivíduo:
Fitness: 158
Cromossomo: [0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
📊 Gráfico salvo como: grafico_com_elitismo.png
```
### 📝 9. Conclusão

Este projeto demonstra a aplicação prática do Algoritmo Genético no problema clássico da mochila, permitindo investigar:
- impacto dos parâmetros (mutação, crossover, população, torneio)
- efeitos de elitismo
- comportamento da convergência via gráficos
  
É um código modular, fácil de expandir e ideal para fins acadêmicos e experimentais.
