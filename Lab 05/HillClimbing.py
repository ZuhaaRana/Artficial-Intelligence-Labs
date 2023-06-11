#Uniform Cost Search Algorithm

from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge_for_UCS(self, u, v, weight):
        #for directed graph
        if self.directed:
            value = (weight, v)
            #print(value)
            self.graph[u].append(value)
        # for undirected graph
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def UCS(self, current_node, goal_node):
        explored = []
        total_cost = 0
        queue_for_cost = PriorityQueue()
        queue_for_cost.put((0, current_node))
        while not queue_for_cost.empty():
            values = queue_for_cost.get()
            current_node = values[1]
            total_cost = total_cost+values[0]
            if current_node == goal_node:
                print(current_node, end=" ")
                print("\nTotal cost of the path is : ",total_cost)
                queue_for_cost.queue.clear()
            else:
                if current_node in explored:
                    continue
                print(current_node, end=" ")
                explored.append(current_node)
                for neighbour in self.graph[current_node]:
                    queue_for_cost.put((neighbour[0], neighbour[1]))

g = Graph(True)
g.add_edge_for_UCS('S', 'A', 1)
g.add_edge_for_UCS('S', 'G', 4)
g.add_edge_for_UCS('A', 'B', 3)
g.add_edge_for_UCS('A', 'C', 1)
g.add_edge_for_UCS('C', 'D', 7)
g.add_edge_for_UCS('B', 'D', 3)
g.add_edge_for_UCS('C', 'G', 2)
g.add_edge_for_UCS('D', 'G', 4)
print("Path for Uniform Cost Search is : ", end=" ")
g.UCS('S', 'G')
