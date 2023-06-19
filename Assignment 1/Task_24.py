
# Task 23
# Plot the given graph
# Note: Use matplotlib or any other python library for plotting graph.

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

G = nx.DiGraph()
G.add_edges_from([('Spider Man','Civil War'),('Spider Man','Iron Man'),('Spider Man','AVENGERS'),
                  ('Iron Man','Civil War'),('Iron Man','AVENGERS'),
                  ('Civil War','Captain America'),('Civil War','Ant Man'),
                  ('Ant Man','Captain America'),('Ant Man','AVENGERS'),
                  ('Captain America','Ant Man'),('Captain America','AVENGERS'),
                  ('AVENGERS','Thor'),('AVENGERS','Hulk'),
                  ('Thor','Ragnarok'),('Ragnarok','Hulk')])
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
plt.show()
