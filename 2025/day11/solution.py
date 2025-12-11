import networkx as nx
from functools import lru_cache

def get_graph():
    G = nx.DiGraph()
    with open("input.txt") as f:
        for line in f:
            connections = line.strip().split()
            for conn in connections[1:]:
                G.add_edge(connections[0][:-1], conn)
    return G

def count_paths_dag(G, source, target):
    @lru_cache(maxsize=None)
    def count_from(node):
        if node == target:
            return 1
        return sum(count_from(neighbor) for neighbor in G.neighbors(node))
    return count_from(source)

def count_paths_with_constraint_dag(G, source, target):
    return count_paths_dag(G, source, "dac") * count_paths_dag(G, "dac", "fft") * count_paths_dag(G, "fft", target) + \
            count_paths_dag(G, source, "fft") * count_paths_dag(G, "fft", "dac") * count_paths_dag(G, "dac", target)

def main():
    G = get_graph()
    num_paths = count_paths_dag(G, "you", "out")
    print(f"Number of paths from you to out: {num_paths}")
    num_paths_constrained = count_paths_with_constraint_dag(G, "svr", "out")
    print(f"Number of paths from svr to out which pass through dac and fft: {num_paths_constrained}")

if __name__ == "__main__":
    main()