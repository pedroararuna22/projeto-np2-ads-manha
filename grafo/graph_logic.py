
# graph_logic.py — você edita APENAS este arquivo nesta atividade.
# Dica: use apenas LISTAS para a fila/estrutura de dados (nada de deque).
# Você pode fazer BFS com:
#   fila = [a]; visitados = [a]
#   while fila:
#       u = fila.pop(0)          # remove o primeiro
#       if u == b: return True
#       for v in graph.get(u, []):
#           if v not in visitados:
#               visitados.append(v)
#               fila.append(v)
#   return False
#
# Alternativamente, pode usar DFS com uma lista como "pilha":
#   pilha = [a]; visitados = []
#   while pilha:
#       u = pilha.pop()          # remove o último
#       ...
#   return False


def connected(graph, a, b):
    if a not in graph or b not in graph:
        return False
    
    fila = [a]
    visitados = [a]

    while fila:
        atual = fila.pop(0)

        if atual == b:
            return True
        
        for vizinho in graph.get(atual, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    return False