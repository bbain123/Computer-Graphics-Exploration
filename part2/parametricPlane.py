from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricPlane(parametricObject):

    #Name: parametricPlane.__init__
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: Initialize all objects of type parametricPlane  
    def __init__(self,T=matrix(np.identity(4)), width = 10.0, length = 10, color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,1.0),vRange=(0.0,1.0),uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__width = width
        self.__length = length

    #Name: parametricPlane.getPoint
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: return the equation of a parametric plane in a 4x4 matrix 
    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0, 0, u*self.__width)
        P.set(1, 0, v*self.__length)
        P.set(2, 0, 0)
        P.set(3, 0, 1)
        return P

    #Name: parametricPlane.setWidth
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the width of the plane
    def setWidth(self, width):
        self.__width = width
    
    #Name: parametricPlane.setLength
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the length of the parametric plane
    def setLength(self, length):
        self.__length = length

    #Name: parametricPlane.getWidth
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: return the planes width   
    def getWidth(self):
        return self.__width

    #Name: parametricPlane.getLength
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: return the planes length
    def getLength(self):
        return self.__length


    