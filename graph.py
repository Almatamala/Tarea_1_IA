# Funcion que carga el archivo y lo convierte en una matriz
def load_edge(file):
    matrix = []
    with open(file) as f:
        for line in f:
            matrix.append(line.split())
    
    return matrix

# Funcion que crea el grafo
def create_edge(data):
    nodes = {} # Inicializa el diccionario de nodos
    edge = {} # Inicializa el diccionario de aristas
    init = data[0][1] # Inicializa el nodo inicial
    goal = data[1][1] # Inicializa el nodo final
    
    data_len = len(data) # Obtiene la longitud de la matriz

    # Crea el diccionario de nodos recorriendo la matriz
    for i in range(2, data_len): 
        if ',' in data[i][0]: # Si encuentra una coma, significa que ya no hay mas nodos, guardamos la posicion y salimos del ciclo
            edge_init = i
            break
        nodes[data[i][0]] = int(data[i][1])
        
    # Crea el diccionario de aristas recorriendo la matriz
    for i in range(edge_init, data_len):
        e = data[i][0].split(',') # separa los nodos y costo de la arista
        if e[0] in edge: # Si el nodo inicial ya esta en el diccionario de aristas, Agrega el nodo final y el costo de la arista
            edge[e[0]][e[1]] = int(e[2]) 
        else: # En caso contrario, crea los nodos y el costo de la arista
            edge[e[0]] = {e[1]: int(e[2])}

    return init,goal,nodes,edge # Retorna el nodo inicial, el nodo final, el diccionario de nodos y el diccionario de aristas