#!/usr/bin/python

from math import sin, pi, cos, log
from cmath import exp

def FFT_dyadic(n, ca): 
  '''n -- number of integers
  ca -- input complex array 
  
  fft -- output complex array 
  
  Recursive algorithm for a dyadic set'''
  fft = []
  if n == 1:
    fft.append(ca[0])
  else:
    ea = [ ca[i] for i in range(0,n,2) ]
    oa = [ ca[i] for i in range(1,n,2) ]

    u = FFT_dyadic(n/2, ea)
    v = FFT_dyadic(n/2, oa)
    
    fft = [0 for i in range(0,n)]
    
    for i in range(0,n):
      tau = exp(2*pi*i*1j/n)
      fft[i] = u[ i%(n/2) ] + tau*v[ i%(n/2) ]
#  print fft
  return fft

def FFT(ca):
    ''' inputs the list and does error checking before the algorithm starts so that it doesn't need to run each time. Also switches between the dyadic and generic methods
    outputs the list that the FFT_dyadic generates '''

    n = len(ca)
    if not ( int(log(n,2)) == log(n,2) ):
      return None

    return FFT_dyadic(n,ca)

def f(x):
  return sin(2*pi*3*x)+ sin(2*pi*x)

if __name__=='__main__':
  array = [ f(i/100.0) for i in range(0,2**10) ]

  #print array
  print FFT(array) # FIX THE TIME REVERSAL
  
