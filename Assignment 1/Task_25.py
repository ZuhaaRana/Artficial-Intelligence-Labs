
# Task 25
# Implement the given graph using adjacency matrix

# Adjacency Matrix representation in Python


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2, weight):
        #if v1 == v2:
            #print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight

    #
    # def __len__(self):
    #     return self.size

    # Print the matrix
    def print_matrix(self):
        print("   " , end=" ")
        for i in range(0 , 7):
            print('{:3}'.format(i), " ", end=" "),
        print()
        print()
        i = 0
        for row in self.adjMatrix:
            print(i , " " , end =" ")
            for val in row:
                print('{:3}'.format(val) , " " , end =" ")
            print()
            i+=1

def main():
    g = Graph(7)
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)

    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)

    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)

    g.add_edge(5, 6, 9)
    g.add_edge(5, 4, 6)

    g.print_matrix()

if __name__ == '__main__':
    main()
