#!/usr/bin/python

visited = []

class T:
  val = None
  nextNodes = []
  def __init__( self, val=None, subT=[] ):
    self.val = val
    self.nextNodes = subT


  # pre-order DFS listing
  def depthFirstSearch( self, first=False ):
    # returns a depth first list
    if first == True:
      del visited[:]
    if not self in visited:
      visited.append(self)
    l = []
    for i in self.nextNodes:
      if not i in visited:
        visited.append(i)
        l = l + i.depthFirstSearch()
    l = [self.val] + l
    return l

def printListWithNums(l):
  return "\n".join( [ " ".join([str(i),str(l[i])])  for i in range(0,len(l))] )


# generation of nodes
a=T('a')
b=T('b')
c=T('c')
d=T('d')
e=T('e')
f=T('f')

# link all nodes together to create graph
a.nextNodes = [b,d,f]
b.nextNodes = [c,f]
c.nextNodes = [d]
d.nextNodes = [b]
e.nextNodes = [d,f]
f.nextNodes = [d]


print "pre-order DFS listing starting with 'a'"
print printListWithNums(a.depthFirstSearch(True))
print "pre-order DFS listing starting with 'e'"
print printListWithNums(e.depthFirstSearch(True))
