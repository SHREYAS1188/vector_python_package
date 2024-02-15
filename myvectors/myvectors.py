import math # used in mag function
from mpl_toolkits.mplot3d import axes3d   # used in draw_vector function 
import matplotlib.pyplot as plt   # used in draw_vector function
import numpy as np   # used in draw_vector function
#%matplotlib inline   # used in draw_vector function


def mag(v1):
        k = math.sqrt(pow(v1[0],2)+pow(v1[1],2)+pow(v1[2],2))
        return(round(k,4))

def dot(v1,v2):
        k = 0
        for i in range(3):
              k = k + v1[i]*v2[i]  
        return round(k,4)

def cross(v1,v2):
        v3 = [0,0,0]
        v3[0] = ((v1[1]*v2[2])-(v2[1]*v1[2]))
        v3[1] = ((v1[0]*v2[2])-(v2[0]*v1[2]))
        v3[2] = ((v1[0]*v2[1])-(v2[0]*v1[1]))
        return(v3)

def projection(v1,v2):
        return(round(dot(v1,v2)/mag(v2),4))

def angle(v1,v2,angle,mode):
        k = dot(v1,v2)/(mag(v1)*mag(v2))
        if ( angle == "cos" ):
                if mode == 0:
                        return(round(math.acos(k),4))
                else:
                        return(round(math.degrees(math.acos(k)),4))
        elif( angle == "sin" ):
                if mode == 0:
                        return(round(math.acos(math.sqrt(1-pow(k,2))),4))
                else:
                        return(round(math.degrees(math.acos(math.sqrt(1-pow(k,2)))),4))

def trianglearea(v1,v2,v3):
        k1= [v2[0] - v1[0] , v2[1] - v1[1] , v2[2] - v1[2]]
        k2= [v3[0] - v1[0] , v3[1] - v1[1] , v3[2] - v1[2]]
        k = 0.5*(mag(cross(k1,k2)))
        return (k)

def sectionsutram(v1,v2,ei,r1,r2):
        v3=[]
        for i in range(3):
                if (ei == 'e'):
                        k = ((r1*v2[i]) + (r2*v1[i]))/(r1+r2)
                elif (ei == 'i'):
                	k = ((r1*v2[i]) - (r2*v1[i]))/(r1-r2)
                v3.append(k)
        return v3

def collinear3(v1,v2,v3):
        k = abs(v2[0] - v1[0])/abs(v2[0] - v3[0]) 
        k1 = abs(v2[1] - v1[1])/abs(v2[1] - v3[1])
        k2 = abs(v2[2] - v1[2])/abs(v2[2] - v3[2])
        k3 = (k/k1)/k2

        if k3:
                return 1
        else:
                return 0

def s_triplepro(v1,v2,v3):
        return(dot(cross(v1,v2),v3))

def v_triplepro(v1,v2,v3):
        return(cross(cross(v1,v2),v3))

'''
edit 2 continues
13:35 hours 
07 april 2021
'''

def draw_vector(v1):

        fig1 = plt.figure()
        ax = fig1.gca(projection='3d')

        x = v1[0]
        y = v1[1]
        z = v1[2]

        u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
        v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
        w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) * np.sin(np.pi * z))

        ax.quiver(x, y, z, u, v, z, length=0.1, normalize=True)
        ax.set_title(' Vector Visualization in 3D space')
        ax.set_xlabel(' X - AXIS ')
        ax.set_ylabel(' Y - AXIS ')
        ax.set_zlabel(' Z - AXIS ')

        plt.show()


'''
edit 3 continues
18:35 hours 
11 january 2023
'''

def direction_Cosine(v1):
        
	ans = [0.0,0.0,0.0]

	den = math.sqrt(pow(v1[0],2)+pow(v1[1],2)+pow(v1[2],2))

	ans[0] = v1[0]/den
	ans[1] = v1[1]/den
	ans[2] = v1[2]/den

	return (ans)

