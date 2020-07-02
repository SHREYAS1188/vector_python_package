import math

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
