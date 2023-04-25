import graph as g
import method as m

def main():
    arg = input('ingrese el nombre del archivo: ')
    data = g.load_edge(arg)
    init,goal,nodes,edge = g.create_edge(data)
    #path, total_cost, expand_count = m.Deep(init, goal, nodes, edge)
    #path, total_cost, expand_count = m.Greedy(init, goal, nodes, edge)
    #path, total_cost, expand_count = m.u_cost(init, goal, nodes, edge)
    path, total_cost, expand_count = m.a_star(init, goal, nodes, edge)
    print(path, total_cost, expand_count)
    
if __name__ == '__main__':
    main()
