#Implement BFS

visited = []
queue = []
#GRAPH = {'A' : ['B','C'],'B' : ['D', 'E'],'C' : ['F'],'D' : [],'E' : ['F'],'F' : []}
GRAPH = {'1' : ['2','3'],'2' : ['4', '5'],'3' : ['6'],'4' : [],'5' : ['6'],'6' : []}
def bfs_algorithm(visited, GRAPH, edge):
  visited.append(edge)
  queue.append(edge)

  while queue:
    popping = queue.pop(0)
    print(popping, " ")

    for connected_node in GRAPH[popping]:
      if connected_node not in visited:
        visited.append(connected_node)
        queue.append(connected_node)

print("Breadth First Search for the given graph is : ", )
bfs_algorithm(visited, GRAPH, '2')
  