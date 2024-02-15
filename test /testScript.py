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
    self.assertEqual(result,1.4906)

    result1 = angle(A,B,"sin",1)
    self.assertEqual(result1,4.5922)

  def test_trianglearea(self):
    A=[1,1,1] 
    B=[1,2,3] 
    C=[2,3,1]
    result = trianglearea(A,B,C)
    self.assertEqual(result, 2.2913)

  def test_sectionsutram(self):
    A=[2,3,4] 
    B=[4,1,-2]
    r1 = 1
    r2 = 2
    ei = i
    result = sectionsutram(A,B,ei,r1,r2)
    expectedResult = [-0.0, 5.0, 10.0]
    self.assertEqual(result, expectedResult)

  def test_collinear(self):
    A=[1,2,3]
    B=[11,8,12]
    C=[10,5,7]
    result = collinear3(A,B,C)
    self.assertEqual(result, 1)

  def test_ScalarTripleProduct(self):
    A=[1,2,3] 
    B=[11,8,12] 
    C=[10,5,7]
    result = s_triplepro(A,B,C)
    self.assertEqual(result,-203)

  def test_VectotTripleProduct(self):
    A=[1,2,3] 
    B=[11,8,12] 
    C=[10,5,7]
    result = v_triplepro(A,B,C)
    expected_result = [-77, 140, 210]
    self.assertEqual(result,expected_result)

  def test_DirectionCosine(self):
    A = [1,2,3]
    result = direction_Cosine(A)
    expected_result = [0.2672612419124244, 0.5345224838248488, 0.8017837257372732]
    self.assertEqual(result,expected_result)
  
  def test_dot(self):
  if __name__ == '__main__':
    unittest.main()
