import unittest
from math import sqrt

#
# Minkowski Distance implementation
#
# See: http://en.wikipedia.org/wiki/Minkowski_distance
#
# Returns the Minkowski distance between two vectors.
# 
# - p : first array
# - q : second array
# - n : distance order
#
# => returns: the distance between p and q.

def minkowski_distance(p, q, n):

    #make sure both array are in the same dimension
    assert len(p) == len(q)  

    return sum([abs(x-y)^n for x,y in zip(p,q)])^1/n

def minkowski_distance_procedural(p, q, n):

    #make sure both array are in the same dimension
    assert len(p) == len(q)  
   
    s = 0  

    for x,y in zip(p,q):

        s += abs(x-y)^n

    return s^(1 / n)

class BinarySearchTest(unittest.TestCase):

      def test_basic(self):
          self.assertEquals(minkowski_distance([1,2,3],[4,5,6],2), 3) 
          self.assertEquals(minkowski_distance_procedural([1,2,3],[4,5,6],1),7) 


if __name__ == '__main__':

      unittest.main()  

