import heapq

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, heuristic):
        self.nodes[name] = {'heuristic': heuristic, 'edges': {}}

    def add_edge(self, from_node, to_node, distance):
        self.nodes[from_node]['edges'][to_node] = distance

    def get_neighbors(self, node):
        return self.nodes[node]['edges']

    def get_heuristic(self, node):
        return self.nodes[node]['heuristic']
    
#  function for loading data from text file into a graph

def load_graph(filename):
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            node = parts[0]
            heuristic = int(parts[1])
            graph.add_node(node, heuristic)
            for i in range(2, len(parts), 2):
                neighbor = parts[i]
                distance = int(parts[i + 1])
                graph.add_edge(node, neighbor, distance)
    return graph

# A* search algorithm starts from below:

def a_star_search(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0 + graph.get_heuristic(start), 0, start, [start]))
    closed_set = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        
        if current in closed_set:
            continue

        closed_set.add(current)

        if current == goal:
            return path, cost

        for neighbor, distance in graph.get_neighbors(current).items():
            if neighbor in closed_set:
                continue
            new_cost = cost + distance
            heapq.heappush(open_set, (new_cost + graph.get_heuristic(neighbor), new_cost, neighbor, path + [neighbor]))

    return None, None

def main():
    graph = load_graph('romaniamap.txt')
    start = input("Start node: ")
    destination = input("Destination node: ")

    path, total_distance = a_star_search(graph, start, destination)
    if path is None:
        print("NO PATH FOUND")
    else:
        print("Path:", " -> ".join(path))
        print("Total distance:", total_distance, "km")

main()
