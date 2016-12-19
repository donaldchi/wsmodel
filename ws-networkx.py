#/usr/bin/env python
import networkx as nx
import sys

p=float(sys.argv[1])
w=open("ws"+str(p)+".txt", "w")
g=nx.watts_strogatz_graph(1000, 5, p)

nx.write_edgelist(g, "ws"+str(p)+".txt", data=False)
