class Graph:
    print("insert number of nodes:")
    n = int(input())
    graph = []
    for i in range(n):
        node = []
        for j in range(n):
            print("insert edge ", j, " value (1 true, 0 false):")
            edge = int(input())
            node.append(edge)
        graph.append(node)
    for i in range(len(graph)):
        print(graph[i])