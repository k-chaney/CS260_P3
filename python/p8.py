#!/usr/bin/python

class T:
  val = None
  nLevel = []
  def __init__( self, val=None, subT=[] ):
    self.val = val
    self.nLevel = subT


  # pre-order DFS listing
  def depthFirstSearch( self ):
    # returns a depth first list
    l = []
    for i in self.nLevel:
      l = l + i.depthFirstSearch()
    l = l + [self.val]
    return l

myT = T(1,[T(2,[ T(4), T(5) ]),T(3) ])
print myT.depthFirstSearch()
