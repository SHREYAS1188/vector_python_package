
# vector_python_package

[![Downloads](https://pepy.tech/badge/myvectors)](https://pepy.tech/project/myvectors)and counting

[[Youtube Video link : Click here](https://youtu.be/Tr-d4uQIgqU)]

[[Example notebook colab link : Click here](https://colab.research.google.com/drive/1brLl8gHiW6yGqMwDKUrsOXMXHm5I_MBW?usp=sharing)]



A python package for vector maths

Installation of the Package

``` python
pip install myvectors 
```

having installed math python library makes the things smoother 

## Package Functionalities

### The vector is represented by **LIST[data structure]** in the package 

#### ex: if v(2,3,4) is a vector at (2,3,4) in space then it should be written as v1=[2,3,4] where v1 is a list 

##### 1.Magnitude of a vector :    A=[2,3,4] magnitude of a given vector
``` python
from myvector import mag
mag(A)
```
Output : float number

##### 2. Dot product : A=[2,3,4]  B = [1,1,2] 
Arguments : two vectors whose dot product is required
``` python
from myvector import dot
dot(A,B)
```

##### 3. Cross product : A=[2,3,4]  B = [1,1,2] 
Arguments : two vectors whose cross product is required
``` python
from myvector import cross
cross(A,B)
```
##### 4.Projection : A=[1,4,0] B=[4,2,4]
Arguments : two vectors here first vector passed as argument is projected over the second vector
```python
from myvector import projection
projection(A,B)
```
Output : number i.e projection of A on B

##### 5.Angle : A=[3,4,-1] B=[2,-1,1] 
Arguments : two vectors , cos/sin , mode(if mode = 0 then angle is in terms of **radian** if mode = 1 then **degrees**)
```python
from myvector import angle
angle(A,B,"cos",0) # angle in terms of cos and radians
angle(A,B,"sin",1) # angle in terms of sin and degrees
```
Output : angle in radians if mode = 0 or in terms of degree if mode = 1

##### 6. Triangle area : the vertices of triangle be A=[1,1,1] B=[1,2,3] C=[2,3,1]
Arguments : the co - ordinates of the vertices of the triangle
```python
from myvector import trianglearea
trianglearea(A,B,C)
```
Output : Area

##### 7.sectionsutram : divide the line joining two points in the ratio r1:r2
A=[2,3,4] B=[4,1,-2]

Arguments : two vectors, ei representing type of division ('e'= external and 'i' = internal),r1,r2 
``` python
from myvector import sectionsutram
sectionsutram(A,B,ei,r1,r2)
```
Output: (A list of length 3) basically vector point with x,y,z co-ordinates

##### 8. collinear or not : checks if three vectors are collinear
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
from myvector import collinear3
collinear3(A,B,C)
 ```
Output : If collinear then output is 1 else 0

##### 9. Scalar Triple Product : if three vectors A,B,C then there scalar triple product is =((AXB)dotproduct(C))
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
from myvector import s_triplepro
s_triplepro(A,B,C)
 ```

##### 10. Vector Triple Product : if three vectors A,B,C then there scalar triple product is =((AXB)XC)
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
from myvector import v_triplepro
v_triplepro(A,B,C)
 ```

