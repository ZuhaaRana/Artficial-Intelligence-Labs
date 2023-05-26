
#Bidirectional Search

class Graph:
    def __init__(self):
        self.graph={}
        self.first_queue=[]
        self.second_queue=[]
        self.first_visited=[]
        self.second_visited=[]
        self.forward_path={}
        self.backward_path={}

    def add_vertex(self):
        for i in range(0, 15):
            g.add_new_vertex(i)

    def add_edge(self):
        g.add_new_edge(0, 2)
        g.add_new_edge(2, 5)
        g.add_new_edge(3, 5)
        g.add_new_edge(5, 6)
        g.add_new_edge(6, 7)
        g.add_new_edge(7, 8)
        g.add_new_edge(8, 10)
        g.add_new_edge(10, 14)

    def add_new_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        else:
           print("Vertex already exists")

    def add_new_edge(self,source,destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def Bidirectional_Algorithm(self):
        array=self.graph.keys()
        array=list(array)
        self.first_queue.append((array[0],''))
        self.second_queue.append((array[len(array)-1],""))
        while self.first_queue!=[] and self.second_queue!=[]:

            first_value= self.first_queue.pop(0)
            second_value=self.second_queue.pop(0)
            
            self.forward_path[first_value[0]]=first_value[1]
            self.backward_path[second_value[0]]=second_value[1]
            
            for child in self.graph[first_value[0]]:
              if child not in self.first_visited:
               self.first_visited.append(child)
               self.first_queue.append((child,first_value[0]))
                    
            for child in self.graph[second_value[0]]:
               if child not in self.second_visited:
                 self.second_visited.append(child)
                 self.second_queue.append((child,second_value[0]))
                    
            intersection = self.common_intersection(self.first_visited,self.second_visited)
            
            if intersection!=[]:
                print("Here the Intersection node is ",end="")
                print(intersection[0])
                Goal=intersection[0]
                print("Path for Bidirectional Search is ")
                
                for x in self.first_queue:
                    if intersection[0]==x[0]:
                        self.forward_path[x[0]]=x[1]
                        break
                        
                for x in self.second_queue:
                    if intersection[0]==x[0]:
                        self.backward_path[x[0]]=x[1]
                        break
                        
                first_Finalpath=[]
                second_Finalpath=[]
                first_Finalpath.append(intersection[0])
                second_Finalpath.append(intersection[0])
                
                for x in self.forward_path:
                  if intersection[0]==0:
                      break
                      
                  first_Finalpath.append(self.forward_path[intersection[0]])
                  intersection[0]=self.forward_path[intersection[0]]
                    
                intersection[0]=Goal
                for x in self.backward_path:
                    if intersection[0] == 14:
                        break
                        
                    second_Finalpath.append(self.backward_path[intersection[0]])
                    intersection[0] = self.backward_path[intersection[0]]
                first_Finalpath.reverse()
                Finalpath=list(dict.fromkeys(first_Finalpath+second_Finalpath))
                print(Finalpath)
                return

    def common_intersection(self, lst1, lst2):
        return list(set(lst1) & set(lst2))

g = Graph()
g.add_vertex()
g.add_edge()
g.Bidirectional_Algorithm()
