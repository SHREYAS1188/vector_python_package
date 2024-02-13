import unittest
import math
from myvectors.myvectors import mag,dot,cross,projection,angle,trianglearea,sectionsutram,collinear3,s_triplepro,v_triplepro

class  testScript(unittest.TestCase):
  def test_mag(self):
    A=[2,3,4]
    result = sum(data)
    self.assertEqual(result, math.sqrt(29))

  def test_dot(self):
    A=[2,-3,4]  
    B = [1,1,2]
    result = dot(A,B)
    self.assertEqual(result,7)

  def test_cross(self):
    A=[2,-3,4]  
    B = [1,1,2]
    result = cross(A,B)
    self.assertEqual(result,1)

  def test_projection(self):
    A=[1,4,0]
    B=[4,2,4]
    result = projection(A,B)
    self.assertEqual(result,2)

  def test_angle(self):
    A=[3,4,-1]
    B=[2,-1,1]
    result = angle(A,B,"cos",0)
    self.assertEqual(result,)

    result1 = angle(A,B,"sin",1)
    self.assertEqual(result1,)
  
  def test_dot(self):
  if __name__ == '__main__':
    unittest.main()
