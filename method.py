import random
import heapq

def Deep(init, goal, nodes, edge): # Busqueda en profundidad
    path = []
    node = init
    total_cost = 0
    expand_count = {node: 0 for node in nodes}
    
    while 1:
        path.append(node)
        expand_count[node] += 1
        
        # Si el nodo es el objetivo, retorna el camino, el costo y cuantas veces fue expandido cada nodo
        if node == goal:
            for i in range(len(path)-1):
                total_cost += edge[path[i]][path[i+1]]

            return path, total_cost, expand_count
        #si el nodo tiene hijos, se escoge uno al azar y se sigue iterando
        if bool(edge[node].keys()):
            node = random.choice(list(edge[node].keys()))
        #si el nodo no tiene hijos, se revisan los nodos anteriores
        else:
            path.pop()
            node = random.choice(list(edge[node].keys()))
#como es busqueda en profundidad, esta hecho para que busque caminos al azar y en caso de que no encuentre el objetivo, entra en un loop infinito

def Greedy(init,goal,nodes,edge): # Busqueda greedy
    path = []
    wrong_path = []
    total_cost = 0
    node = init
    expand_count = {node: 0 for node in nodes}

    while len(wrong_path) != len(nodes):
        
        path.append(node)
        expand_count[node] += 1
        
        # Si el nodo es el objetivo, retorna el camino, el costo y cuantas veces fue expandido cada nodo
        if node == goal:
            for i in range(len(path)-1):
                total_cost += edge[path[i]][path[i+1]]

            return path, total_cost, expand_count
        #si el nodo tiene hijos, escoge el que tiene la heuristica de menor costo, 
        #no vuelve a tomar el mismo camino de antes
        if bool(edge[node].keys()):
            H = []
            for child in edge[node].keys():
                H.append((child, nodes[child]))
            Hsort = sorted(H, key=lambda x: x[1])
            for child in Hsort[0]:
                node = child
                if child not in wrong_path:
                    break
        #si el nodo no tiene hijos, se revisan los nodos anteriores
        else:
            wrong_path.append(path.pop())
      
    return None, None, None                

def u_cost(init,goal,nodes,edge): # Busqueda de costo uniforme
    # Lista de nodos a expandir que guarda el nodo actual, costo acumulado y el camino
    node_list = [(init, 0, [init])] 
    expand_count = {node: 0 for node in nodes}

    while node_list:

        # Ordena la lista de nodos por costo acumulado
        node_list.sort(key=lambda x: x[1])

        # Obtiene el nodo con menor costo
        node, cost, path = node_list.pop(0)

        # Si el nodo es el objetivo, retorna el camino, el costo y cuantas veces fue expandido cada nodo
        if node == goal:
            return path, cost, expand_count

        expand_count[node] += 1
    
        # recorre los nodos hijos del nodo actual
        for nxt in edge[node]:
            # Si el nodo no esta en la lista de nodos a expandir, lo agregamos
            if not any(nxt in sublist for sublist in node_list):
                node_list.append((nxt, cost + edge[node][nxt], path + [nxt]))
            # Si el nodo esta en la lista de nodos a expandir, revisamos si el costo es menor
            elif any(nxt in sublist for sublist in node_list):
                x = node_list.index((nxt,)) if (nxt,) in node_list else -1
                #en caso de que lo sea, sacamos el nodo que llego al mismo nodo pero por un camino mas costoso, 
                #caso contrario nos quedamos con el que ya estaba
                if cost + edge[node][nxt] < node_list[x][1]:
                    node_list.pop(x)
                    node_list.append((nxt, cost + edge[node][nxt], path + [nxt]))       
    # si no existe el nodo objetivo, se vaciara la lista y se retornara None
    return None, None, None 


def a_star(init, goal, nodes, edge): #busqueda A*
    # Lista de nodos a expandir que guarda el nodo actual, costo acumulado y el camino
    node_list = [(init, 0, [init])] 
    expand_count = {node: 0 for node in nodes}

    while node_list :

        # Ordena la lista segun la funcion f(n) = g(n) + h(n) 
        node_list.sort(key=lambda f: f[1] + nodes[f[0]])
        # Obtiene el nodo con menor costo
        node, cost, path = node_list.pop(0)
        # Si el nodo es el objetivo, retorna el camino y el costo
        if node == goal:
            return path, cost, expand_count

        expand_count[node] += 1 
        
        for nxt in edge[node]:
            # Si el nodo no esta en la lista de nodos a expandir, lo agregamos
            if not any(nxt in sublist for sublist in node_list):
                node_list.append((nxt, cost + edge[node][nxt], path + [nxt]))
            # Si el nodo esta en la lista de nodos a expandir, revisamos si el costo es menor
            elif any(nxt in sublist for sublist in node_list):
                x = node_list.index((nxt,)) if (nxt,) in node_list else -1
                #en caso de que lo sea, sacamos el nodo que llego al mismo nodo pero por un camino mas costoso, 
                #caso contrario nos quedamos con el que ya estaba
                if cost + edge[node][nxt] < node_list[x][1]:
                    node_list.pop(x)
                    node_list.append((nxt, cost + edge[node][nxt], path + [nxt]))    
    # si no existe el nodo objetivo, se vaciara la lista y se retornara None
    return None, None, None
