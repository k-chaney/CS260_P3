#!/usr/bin/env python

from array import *

class ListArray:
  #Max length
  MAX_LENGTH = 200000
  #Integer array
  elements = array('i')
  #Equivalent to the last usable index
  last = -1
  
  def __init__(self):
    #Init to maxmimum static size
    self.elements = [0]*self.MAX_LENGTH
    return
  
  def insert(self,x,p):
    if not(self.last < self.MAX_LENGTH -1) :
      print "List-Array.insert: Array already at maximum size: ",self.MAX_LENGTH
    elif p <=self.last+1 and p>=0:
      for i in range(self.last,p-1,-1):
	self.elements[i+1] = self.elements[i]
      self.elements[p] = x
      self.last = self.last + 1
    else:
      print "List-Array.insert: Index out of range: ", p, ". Length:",self.last+1
    return

  def locate(self,x):
    for i in range(0,self.last+1):
      if self.elements[i]==x:
	  return i;
    #Not found
    return self.end()
    
  def retrieve(self,p):
    if p <=self.last and p>= 0:
      return self.elements[p]
    else:
      return
    
  def delete(self,p):
    if p <=self.last and p>= 0:
      for i in range(p+1,self.last+1):
	self.elements[i-1] = self.elements[i]
      self.last = self.last - 1
    return

  def next_item(self,p):
    if p < self.last and p >= 0:
      return p+1
    else:
      return self.end()
    
  def previous(self,p):
    if p <= self.last and p > 0:
      return p-1
    else:
      return self.end()
    
  def makenull(self):
    self.__init__()
    return
  
  def first(self):
    if self.last >=0:
      return 0
    else:
      return self.end()
    
  def printlist(self):
    for i in range(0,self.end()):
      print self.elements[i]
    return
    
  def end(self):
    #Return one past the last usable index
    return self.last+1
    

