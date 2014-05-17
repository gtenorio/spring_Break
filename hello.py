from collections import deque #library importing

''' #Hello World and basic arrays
print "Hello World!"
array = [0,1,2,3,4]
for i in array:
  print i
  print "still in for loop" #notice it's space sensitive
print "End of for loop " \
        "two lined printp"
'''

''' # QUEUE stuff
queue = deque([0,1,2,3,4,5,6])
print queue
queue.append(99)
queue.append(100)
for i in range(0,5):
  print '{} is being popped.'.format(queue.popleft())
print queue
'''

a = []
for i in xrange(3):
  a.append([])
  for j in xrange(3):
    a[i].append(i+j)
print a

blah = 'FALSE'
if (blah == 'FALSE'):
  print "it's false"

