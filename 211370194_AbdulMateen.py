import heapq

# Graph class for cities' map

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

"""
    following code was working fine but there was an edge case for cities name having spaces in them

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

Below code will use a different strategy to separate cities instead of on the basis of spaces

"""
def load_graph(filename):
    graph = Graph()

    with open(filename, 'r') as file:

        for line in file:
            parts = line.strip().split()
           
            for i, part in enumerate(parts):
                if part.isdigit():
                    heuristic_index = i
                    break

            node = ' '.join(parts[:heuristic_index])
            heuristic = int(parts[heuristic_index])
            graph.add_node(node, heuristic)
          
            edges_parts = parts[heuristic_index + 1:] 
            i = 0

            while i < len(edges_parts):
                
                if edges_parts[i].isdigit():
                    distance = int(edges_parts[i])
                    neighbor = ' '.join(edges_parts[:i]) 
                    graph.add_edge(node, neighbor, distance)
                    edges_parts = edges_parts[i+1:] 
                    i = 0 
                else:
                    i += 1

    return graph

# A* search algorithm starts from below:

def a_star_search(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0 + graph.get_heuristic(start), 0, start, [start]))
    explored = set()

    while frontier:
        _, cost, current, path = heapq.heappop(frontier)
        
        if current in explored:
            continue

        explored.add(current)

        if current == goal:
            return path, cost

        for neighbor, distance in graph.get_neighbors(current).items():

            if neighbor in explored:
                continue

            new_cost = cost + distance
            heapq.heappush(frontier, (new_cost + graph.get_heuristic(neighbor), new_cost, neighbor, path + [neighbor]))

    return None, None

def main():
    graph = load_graph('romaniamap.txt')
    start = input("Please enter name of the starting city: ").capitalize()
    destination = input("Please enter name of the destination city: ").capitalize()

    if start not in graph.nodes:
        print(f"Start node '{start}' does not exist in the graph.")
        return 
    
    if destination not in graph.nodes:
        print(f"Destination node '{destination}' does not exist in the graph.")
        return

    path, total_distance = a_star_search(graph, start, destination)

    if path is None:
        print("NO PATH FOUND")
    else:
        print("\n\n----------Following is the information of your path and the total distance----------\n")
        print("Path:", " -> ".join(path))
        print("Total distance:", total_distance, "km")

main()
