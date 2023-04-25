import graph as g
import method as m

def main():
    arg = input('ingrese el nombre del archivo: ')    
    arg_method = input('ingrese el metodo a usar (deep,greedy,ucost,astar): ')
    data = g.load_edge(arg)
    init,goal,nodes,edge = g.create_edge(data)
    while 1:
        if arg_method == 'deep':
            print('busqueda en profundidad')
            path, total_cost, expand_count = m.Deep(init, goal, nodes, edge)
            break
        elif arg_method == 'greedy':
            print('busqueda greedy')
            path, total_cost, expand_count = m.Greedy(init, goal, nodes, edge)
            break
        elif arg_method == 'ucost':
            print('busqueda por costo uniforme')
            path, total_cost, expand_count = m.u_cost(init, goal, nodes, edge)
            break
        elif arg_method == 'astar':
            print('busqueda A*')
            path, total_cost, expand_count = m.a_star(init, goal, nodes, edge)
            break
        else:
            print('metodo no valido')
            arg_method = input('ingrese el metodo a usar: ') 
    print(path, total_cost, expand_count)
    
if __name__ == '__main__':
    main()
