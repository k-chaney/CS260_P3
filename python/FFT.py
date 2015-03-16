#!/usr/bin/python

from math import sin, pi, cos, log
from cmath import exp

# need this for the generic case--this is a "good enough" function
def factors(n):    
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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

def FFT(n,ca):
  ''' ca -- input complex array '''
  fft = []
  factor_list = sorted(list(factors(n))) # unless this is a very large number this isn't too bad
  if(len(factor_list)==2):
    fft = [0 for i in range(0,n)]
    for i in range(0,n):
      fft[i] =   sum([ ca[k]*exp(2.0*pi*1j/n*i*k).conjugate() for k in range(0,n) ] )
  else:
    r1 = factor_list[len(factor_list)/2] # do something smart here  n = r1*r2
    r2 = n/r1
    a = [ None for i in range(0,r1) ]
    for k in range(0,r1):
      a[k] = FFT(r2, ([ca[k+(r1*(r2-i))] for i in range(1,r2+1) ][::-1]) )
    fft = [0 for i in range(0,n)]
    for i in range(0,n):
      fft[i] = sum( [ a[k][i%r2]*exp(2.0*pi*1j/n*i*k).conjugate() for k in range(0,r1) ] )
  return fft

def f(x):
  return sin(2*pi*3*x)+ sin(2*pi*x)

if __name__=='__main__':
  array = [ f(i/1000) for i in range(0,5555) ]

  print array
  print FFT(len(array),array)
  
