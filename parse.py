f = open('graph.txt', 'r')

for line in f:
  print line,
  print 'vertex:', line[0]
  print 'adj:',
  for letter in line[4:]:
    if(letter != ' ') or (letter != '|'):
      print letter,
  print ' '
