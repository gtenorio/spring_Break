import sys
from collections import deque

class vertex:
  label, BFS_num, pi, adj = 'NA', sys.maxint, 'NIL', []
  def __init__(self, node, num, parent, adjct):
    self.label = node
    self.BFS_num = num
    self.pi = parent
    self.adj = adjct
  def display(self):
    print self.label, self.adj, self.BFS_num, self.pi


f = open('graph.txt', 'r')

graph = []
f = open('graph.txt', 'r')
for line in f:
  temp = []
  for letter in line[4:]:
    if (letter != ' ') and (letter != '|') and (letter != '\n'): 
      temp.append(letter)
  graph.append(vertex(line[0], sys.maxint, 'NIL',temp))

print "\ninput:"
for node in graph:
  node.display()

queue = []
#begin BFS, assume A is source
graph[0].BFS_num = 0;

queue = deque(graph[0].label)

while (len(queue) > 0):
  temp = queue.popleft()
  for g in graph:
    if (temp == g.label):
      for i in g.adj:
        for neighbor in graph:
          if(i == neighbor.label) and (neighbor.BFS_num == sys.maxint):
            neighbor.BFS_num = g.BFS_num + 1
            neighbor.pi = g.label
            queue.append(neighbor.label)

print "\noutput:"
for every in graph:
  every.display()
