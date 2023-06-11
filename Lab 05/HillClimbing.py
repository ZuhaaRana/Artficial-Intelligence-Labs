#Hill Climbing Algorithm

from collections import defaultdict

class Graph:
    def __init__(self, total_vertices):
        global start
        self.graph = defaultdict(list)
        self.vertices = total_vertices
        self.explored = []
        self.total_cost = 0
        self.path_for_climbing = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def add_all_edges(self):
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('A', 'D')
        g.add_edge('B', 'A')
        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'A')
        g.add_edge('C', 'B')
        g.add_edge('C', 'D')
        g.add_edge('D', 'A')
        g.add_edge('D', 'B')
        g.add_edge('D', 'C')

    def add_values(self):
        actualValues = {'AB': 25, 'AD': 15, 'BD': 45, 'BC': 10, 'CD': 5, 'AC': 10, 'BA': 25, 'DA': 15, 'DB': 45,
                        'CB': 10, 'DC': 5, 'CA': 10, }

    def find_actual_path_value(self, optimal_path):
        for i in range(len(optimal_path)-1):
            self.total_cost += g.add_values([optimal_path[i]+optimal_path[i+1]])
        return self.total_cost

    def all_sol(self,explored, visited):
        self.explored.append(visited)
        for i in self.graph[visited]:
            if not self.explored:
                print(len(self.path_for_climbing))
            if i not in self.explored:
                self.all_sol(self.explored.copy(), i)
            else:
                if len(self.explored) == self.vertices:
                    if self.explored not in self.path_for_climbing and start in self.graph[self.explored[len(self.explored) - 1]]:
                        self.explored.append(start)
                        self.path_for_climbing.append(self.explored)

    def hill_climbing(self):
        start = "D"
        self.all_sol( self.explored,start)
        if not len(self.path_for_climbing):
            print("No Path.")
            return
        cost = self.find_actual_path_value(self.path_for_climbing[0])
        self.optimal_path()
    
    def optimal_path(self):
        for i in range(1, len(self.path_for_climbing)):
            current_path = self.find_actual_path_value(self.path_for_climbing[i])
            if current_path < cost:
                cost = current_path
                continue
            else:
                break
        print(f"Best Cost of Travelling is : {self.path_for_climbing[i-1]}")
        print("The cost of this path is : ", cost)

g = Graph(4)
g.add_all_edges()
g.add_values()
g.hill_climbing()
