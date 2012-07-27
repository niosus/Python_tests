import math
import numpy


    
class Point:
  def __init__(self, P):
    self.coor =numpy.array(P)
  def out(self, name=''):
    print name+' Point'
    print self.coor
  def __add__(self, other): 
    return self.coor+other.coor
  def __sub__(self, other): 
    return self.coor-other.coor
    
class Plane:
  def __init__(self, N, P):
    self.normal = numpy.array(N)
    self.point = Point(P)
  def out(self):
    print 'Plain normal'
    print self.normal
    self.point.out('Plain')
    
def FindIntersection(plain,point1,point2):
  
  u=numpy.dot(plain.normal, plain.point-point1)/numpy.dot(plain.normal, point2-point1)
  print 'u = %f' % u
  return point1+Point(u*(point2-point1))
    
Z = Plane([0,0,1],[0,0,0])
P1 = Point([0,0,4])
P2 = Point([1,0,2])
Z.out()
P1.out('First')
P2.out('Second')
intersection=FindIntersection(Z,P1,P2)
print intersection
