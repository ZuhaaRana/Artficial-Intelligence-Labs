
#A Star Search Algorithm

class Graph:
    def __init__(self):
        self.vertices_no = 0
        self.graph = {}
        self.heuristic = {}

    def add_new_vertices(self):
        g.add_vertex('A', 25)
        g.add_vertex('B', 6)
        g.add_vertex('C', 13)
        g.add_vertex('D', 20)
        g.add_vertex('E', 18)
        g.add_vertex('F', 28)
        g.add_vertex('G', 0)

    def add_edges(self):
        g.add_edge('A', 'B', 11)
        g.add_edge('A', 'C', 14)
        g.add_edge('A', 'D', 7)
        g.add_edge('B', 'E', 15)
        g.add_edge('C', 'E', 8)
        g.add_edge('C', 'F', 10)
        g.add_edge('D', 'F', 25)
        g.add_edge('E', 'H', 9)
        g.add_edge('F', 'G', 20)
        g.add_edge('H', 'G', 10)

    def add_vertex(self,Vertex, heuristic_value):
        if Vertex in self.graph:
            print("Vertex Already Exists")
        else:
            self.graph[Vertex] = []
            self.heuristic[Vertex] = heuristic_value
            self.vertices_no += 1

    def add_edge(self,first_vertex, second_vertex, calculated_cost):
        if first_vertex not in self.graph:
            return
        elif second_vertex not in self.graph:
            return
        else:
            self.graph[first_vertex].append((second_vertex,calculated_cost))
            self.graph[second_vertex].append((first_vertex,calculated_cost))
            
    def print_path(self,S,P):
        new = "G"
        A_path = ["G"]
        while new != S:
            A_path.append(P[new])
            new = P[new]
        A_path.reverse()
        print(A_path)

    def AS_Algorithm(self,start):
        Visited = []
        first_queue = []
        second_queue = []
        Parent = {}

        first_queue.append((start, 0, -1))
        second_queue.append(0+self.heuristic[start])

        while len(first_queue) != 0:
            vertices = first_queue.pop(second_queue.index(min(second_queue)))

            if vertices[0] not in Visited:
                Visited.append(vertices[0])
                Parent[vertices[0]] = vertices[2]
            else:
                continue
            if vertices[0] == "G":
                #print("Goal is achieved.")
                break
            for i in self.graph[vertices[0]]:
                if i[0] not in Visited:
                    i = list(i)
                    i[1] += vertices[1]
                    i = (i[0], i[1], vertices[0])
                    first_queue.append(i)
                    second_queue.append(i[1] + self.heuristic[i[0]])
        g.print_path(start,Parent)


g = Graph()
print("Path for A* Search is ")
g.add_new_vertices()
g.add_edges()
g.AS_Algorithm("B")
