#!/usr/bin/env python3

import random
random.seed()

#n = int(input('#Nodes: '))
#k2 = int(input('Degree/2: '))
#p = float(input('p: '))
n = 10000
k2=4
p=0.01

nodes, edges = [], []

for i in range(0, n):
  node = []
  for j in range(i - k2, i + k2 + 1):
    j2 = (j + n) % n
    if i != j2:
      node.append(j2)
    if i < j:
      edges.append([i, j2])
  nodes.append(node)

E = len(edges)
assert E == n * k2
assert len(nodes) == n

n_rewire = int(n * p)
while n_rewire > 0:
  r = random.randint(0, E - 1)
  e0 = edges[r]
  f = e0[int(r > n/2)]
  e1 = [f, f]
  while e1[0] == e1[1] or e1[1] in nodes[e1[0]]:
    e1[1] = random.randint(0, n-1)
    e1.sort()
  edges.pop(r)
  nodes[e0[0]].remove(e0[1])
  nodes[e0[1]].remove(e0[0])
  edges.append(e1)
  nodes[e1[0]].append(e1[1])
  nodes[e1[1]].append(e1[0])
  n_rewire = n_rewire - 1

for f, t in edges:
  print('{0}, {1}'.format(f, t))
