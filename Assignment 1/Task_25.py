
# Task 24
# Implement given graph using adjacency list

#Here the values of the nodes/vertices are assigned as :
#Vertex 0 = A, Vertex 1 = B, Vertex 2 = C, Vertex 3 = D, Vertex 4 = E, 
Vertex 5 = F, Vertex 6 = G, Vertex 7 = H

class new_node:
    def __init__(self, value):
        self.vertex = value

class Graph:
    def __init__(self, num):
        self.TOTAL_VERTICES = num
        self.graph = [None] * self.TOTAL_VERTICES

    def add_new_edge(self, x, y):
        node = new_node(y)
        node.next = self.graph[x]
        self.graph[x] = node
        node = new_node(x)
        node.next = self.graph[y]
        self.graph[y] = node

    def display(self):
        for i in range(self.TOTAL_VERTICES):
            print("Vertex " + str(i) + ":", end="")
            NEXT = self.graph[i]
            while NEXT:
                print(" -> {}".format(NEXT.vertex), end="")
                NEXT = NEXT.next
            print(" \n")

TOTAL_VERTICES = 8

G = Graph(TOTAL_VERTICES)
G.add_new_edge(0, 1)
G.add_new_edge(0, 2)
G.add_new_edge(0, 3)
G.add_new_edge(1, 4)
G.add_new_edge(1, 5)
G.add_new_edge(4, 6)
G.add_new_edge(5, 7)

G.display()
