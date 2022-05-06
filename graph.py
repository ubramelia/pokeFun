from collections import defaultdict

class Graph:
    graph = defaultdict(list)
    def addEdge(graph,u,v):
        graph[u].append(v)

    def generate_edges(graph):
        edges = []

        for node in graph:
            for neighbour in graph[node]:
                edges.append((node, neighbour))
        return edges