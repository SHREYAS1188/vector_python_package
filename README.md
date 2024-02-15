
# vector_python_package  
:V:E:C:T:O:R:S: made easy
This version 1.2 is named as "Shobha" 
*****
![Static Badge](https://img.shields.io/badge/Made%20With%20Love%20In%20INDIA%20%E2%9D%A4-FF9933)
[![My Skills](https://skillicons.dev/icons?i=python&theme=dark)](https://skillicons.dev) 
 [![Downloads](https://static.pepy.tech/badge/myvectors)](https://pepy.tech/project/myvectors) 
![Static Badge](https://img.shields.io/badge/version-1.2-blue)
[![Downloads](https://static.pepy.tech/badge/myvectors/month)](https://pepy.tech/project/myvectors)
![Static Badge](https://img.shields.io/badge/coverage-93%25-green)




****
A python package for vector maths

#### Installation of the Package

``` python
pip install myvectors 
```

having installed "math" python library makes the things smoother 

***
** Youtube Video Tutorials
(https://youtube.com/playlist?list=PL6LEAq5DrlOScWUPGQ4YHr-naw-H7OtKz)
(https://youtu.be/Tr-d4uQIgqU)

** Colab Notebook (dont forget to check the colab notebook)
(https://colab.research.google.com/drive/1brLl8gHiW6yGqMwDKUrsOXMXHm5I_MBW?usp=sharing)

** Please Give feedback about the library "myvectors", your feedback is highly valuable
(https://forms.gle/P9kwsYUQJvuC9qXb6)
*****



## Package Functionalities

### The vector is represented by **LIST[data structure]** in the package 

#### ex: if v(2,3,4) is a vector at (2,3,4) in space then it should be written as v1=[2,3,4] where v1 is a list 

##### 1.Magnitude of a vector :    A=[2,3,4] magnitude of a given vector
``` python
import myvectors
from myvectors import mag
A = [2,3,4]
mag(A)
```
output : float number

##### 2. Dot product : A=[2,3,4]  B = [1,1,2] 
Arguments : two vectors whose dot product is required
``` python
import myvectors
A = [2,3,4]  
B = [1,1,2]
from myvectors import dot
dot(A,B)
```
output : float number
##### 3. Cross product : A=[2,3,4]  B = [1,1,2] 
Arguments : two vectors whose cross product is required
``` python
import myvectors
A = [2,3,4]  
B = [1,1,2] 
from myvectors import cross
cross(A,B)
```
output : list
##### 4.Projection : A=[1,4,0] B=[4,2,4]
Arguments : two vectors here first vector passed as argument is projected over the second vector
```python
import myvectors
A = [1,4,0] 
B = [4,2,4]
from myvectors import projection
projection(A,B)
```
output : number i.e projection of A on B

##### 5.Angle : Gives Angle between two vectors A=[3,4,-1] B=[2,-1,1] 
Arguments : two vectors , cos/sin , mode(if mode = 0 then angle is in terms of **radian** if mode = 1 then **degrees**)
```python
import myvectors
from myvectors import angle
A = [3,4,-1] 
B = [2,-1,1] 
angle(A,B,"cos",0) # angle in terms of cos and radians
angle(A,B,"sin",1) # angle in terms of sin and degrees
```
output : angle in radians if mode = 0 or in terms of degree if mode = 1

##### 6. Triangle area : the vertices of triangle be A=[1,1,1] B=[1,2,3] C=[2,3,1]
Arguments : the co - ordinates of the vertices of the triangle
```python
import myvectors
A = [1,1,1] 
B = [1,2,3] 
C = [2,3,1]
from myvectors import trianglearea
trianglearea(A,B,C)
```
output : Area (float number)

##### 7.sectionsutram : divide the line joining two points in the ratio r1:r2 A=[2,3,4] B=[4,1,-2]

Arguments : two vectors, ei representing type of division ('e'= external and 'i' = internal),r1,r2 
``` python
import myvectors
A = [2,3,4] 
B = [4,1,-2]
r1 = 1
r2 = 2
ei = 'i' #ei = 'i' for internal , ei= 'e' for external
from myvectors import sectionsutram
sectionsutram(A,B,ei,r1,r2)
```
output: (A list of length 3) basically vector point with x,y,z co-ordinates

##### 8. collinear or not : checks if three vectors are collinear
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
import myvectors
A = [1,2,3] 
B = [11,8,12] 
C = [10,5,7]
from myvectors import collinear3
collinear3(A,B,C)
 ```
output : If collinear then output is 1 else 0

##### 9. Scalar Triple Product : if three vectors A,B,C then there scalar triple product is =((AXB)dotproduct(C))
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
import myvectors
A = [1,2,3] 
B = [11,8,12] 
C = [10,5,7]
from myvectors import s_triplepro
s_triplepro(A,B,C)
 ```
 output : float number

##### 10. Vector Triple Product : if three vectors A,B,C then there scalar triple product is =((AXB)XC)
A=[1,2,3] B=[11,8,12] C=[10,5,7]
```python
import myvectors
A = [1,2,3] 
B = [11,8,12] 
C = [10,5,7]
from myvectors import v_triplepro
v_triplepro(A,B,C)
 ```
 output : list[x,y,z]

##### 11. Vector visualization in 3D space: A given vector say 'V' is visualized in 3-Dimensional space
A = [0,0,2]
```python
import myvectors
A = [0,0,2]
from myvectors import draw_vector
draw_vector(A)
```
output : A vector representation in 3-D space.
![output_draw_vector](/img/draw_vectors.png)

##### 12. Vector Direction Cosines: Given a vector 'V' it gives the diection cosine
A = [1,2,3]
```python
import myvectors
A = [1,2,3]
from myvectors import direction_Cosine
direction_Cosine(A)
```
output : list[x,y,z]

************

