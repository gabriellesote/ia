import random
import heapq

# ==============================================================================
# 1. CÓDIGOS BASE FORNECIDOS
# ==============================================================================

def generate_grid(n, p):
    """Gera uma grade aleatória n x n com uma probabilidade 'p' de obstáculos."""
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                grid[i][j] = 1  # 1 representa um obstáculo
    
    # Garante que o início (0,0) e o fim (n-1, n-1) não sejam obstáculos
    grid[0][0] = 0
    grid[n-1][n-1] = 0
    return grid

def manhattan_distance(p1, p2):
    """Calcula a distância de Manhattan entre dois pontos (tuplas)."""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def print_grid_with_path(grid, path, start, goal):
    """
    Visualiza a grade com o caminho encontrado.
    '.' -> Célula livre
    '#' -> Obstáculo
    'S' -> Início
    'G' -> Objetivo (Goal)
    'X' -> Caminho percorrido
    """
    n = len(grid)
    grid_str = ""
    for r in range(n):
        row_str = []
        for c in range(n):
            if (r, c) == start:
                row_str.append("S")
            elif (r, c) == goal:
                row_str.append("G")
            elif path and path[r][c]:
                row_str.append("X")
            elif grid[r][c] == 1:
                row_str.append("#")
            else:
                row_str.append(".")
        grid_str += " ".join(row_str) + "\n"
    print(grid_str)

# ==============================================================================
# 2. IMPLEMENTAÇÃO DAS HEURÍSTICAS
# ==============================================================================

def get_valid_neighbors(grid, cell):
    """Retorna os vizinhos válidos (dentro dos limites e não-obstáculos) de uma célula."""
    n = len(grid)
    x, y = cell
    neighbors = []
    # Movimentos: Cima, Baixo, Esquerda, Direita
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        # Verifica se está dentro da grade
        if 0 <= nx < n and 0 <= ny < n:
            # Verifica se não é um obstáculo
            if grid[nx][ny] == 0:
                neighbors.append((nx, ny))
    return neighbors

# ------------------------------------------------------------------------------
# 2.1 HEURÍSTICA: HILL CLIMBING (SUBIDA DE ENCOSTA)
# ------------------------------------------------------------------------------

def hill_climbing(grid, start, goal):
    """
    Implementa a busca Hill Climbing.
    Move-se sempre para o vizinho mais próximo do objetivo.
    Para se não houver um vizinho melhor que a posição atual.
    """
    n = len(grid)
    current_cell = start
    path_list = [start]
    
    while current_cell != goal:
        neighbors = get_valid_neighbors(grid, current_cell)
        
        # Filtra vizinhos que já estão no caminho para evitar loops simples
        neighbors = [n for n in neighbors if n not in path_list]

        if not neighbors:
            print("Hill Climbing: Preso! Sem vizinhos válidos para se mover.")
            break

        # Calcula a distância de Manhattan de cada vizinho até o objetivo
        neighbor_distances = {neighbor: manhattan_distance(neighbor, goal) for neighbor in neighbors}
        
        # Encontra o melhor vizinho (menor distância)
        best_neighbor = min(neighbor_distances, key=neighbor_distances.get)
        
        # Distância do melhor vizinho vs. distância da célula atual
        if neighbor_distances[best_neighbor] >= manhattan_distance(current_cell, goal):
            print("Hill Climbing: Preso em um mínimo local/plateau.")
            break
            
        current_cell = best_neighbor
        path_list.append(current_cell)

    # Constrói a matriz booleana do caminho para visualização
    path_grid = [[False] * n for _ in range(n)]
    for x, y in path_list:
        path_grid[x][y] = True
        
    return path_grid, path_list

# ------------------------------------------------------------------------------
# 2.2 HEURÍSTICA: BEST-FIRST SEARCH (BUSCA GULOSA)
# ------------------------------------------------------------------------------

def best_first_search(grid, start, goal):
    """
    Implementa a busca Best-First (Gulosa).
    Usa uma fila de prioridade para sempre explorar o nó mais próximo do objetivo
    de acordo com a heurística (distância de Manhattan).
    """
    n = len(grid)
    
    # Fila de prioridade: (distancia_heuristica, (x, y))
    priority_queue = [(manhattan_distance(start, goal), start)]
    heapq.heapify(priority_queue)
    
    # Dicionário para reconstruir o caminho
    came_from = {start: None}
    
    # Conjunto para rastrear células já visitadas
    visited = {start}

    while priority_queue:
        # Pega a célula da fila com a menor distância heurística
        _, current_cell = heapq.heappop(priority_queue)

        if current_cell == goal:
            break  # Objetivo alcançado

        for neighbor in get_valid_neighbors(grid, current_cell):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current_cell
                priority = manhattan_distance(neighbor, goal)
                heapq.heappush(priority_queue, (priority, neighbor))
    
    # Se o objetivo foi alcançado, reconstrói o caminho
    path_list = []
    if goal in came_from:
        path_cursor = goal
        while path_cursor is not None:
            path_list.append(path_cursor)
            path_cursor = came_from[path_cursor]
        path_list.reverse()

    # Constrói a matriz booleana do caminho para visualização
    path_grid = [[False] * n for _ in range(n)]
    for x, y in path_list:
        path_grid[x][y] = True
        
    return path_grid, path_list

# ==============================================================================
# 3. EXECUÇÃO E COMPARAÇÃO
# ==============================================================================

if __name__ == "__main__":
    # Parâmetros da simulação
    GRID_SIZE = 10
    OBSTACLE_PROBABILITY = 0.25 # 25% de chance de uma célula ser um obstáculo
    
    # Definindo início e fim
    START_NODE = (0, 0)
    GOAL_NODE = (GRID_SIZE - 1, GRID_SIZE - 1)
    
    # Gerar a grade
    grid = generate_grid(GRID_SIZE, OBSTACLE_PROBABILITY)
    
    print("="*40)
    print(f"GRADE GERADA ({GRID_SIZE}x{GRID_SIZE})")
    print("S = Início, G = Fim, # = Obstáculo")
    print_grid_with_path(grid, None, START_NODE, GOAL_NODE)
    print("="*40)
    
    # --- Executando Hill Climbing ---
    print("\n" + "-"*10 + " EXECUTANDO HILL CLIMBING " + "-"*10)
    hc_path_grid, hc_path_list = hill_climbing(grid, START_NODE, GOAL_NODE)
    
    if hc_path_list and hc_path_list[-1] == GOAL_NODE:
        print(f"Sucesso! Caminho encontrado com {len(hc_path_list)} passos.")
    else:
        print(f"Não foi possível encontrar o caminho. O algoritmo parou em {hc_path_list[-1]}.")
        
    print_grid_with_path(grid, hc_path_grid, START_NODE, GOAL_NODE)
    
    # --- Executando Best-First Search ---
    print("\n" + "-"*10 + " EXECUTANDO BEST-FIRST SEARCH " + "-"*10)
    bfs_path_grid, bfs_path_list = best_first_search(grid, START_NODE, GOAL_NODE)

    if bfs_path_list and bfs_path_list[-1] == GOAL_NODE:
        print(f"Sucesso! Caminho encontrado com {len(bfs_path_list)} passos.")
    else:
        print("Não foi possível encontrar um caminho até o objetivo.")

    print_grid_with_path(grid, bfs_path_grid, START_NODE, GOAL_NODE)
