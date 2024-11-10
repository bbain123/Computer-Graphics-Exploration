from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCircle(parametricObject):

    #Name: parametricCircle.__init__
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: Initialize all objects of type parametricCircle 
    def __init__(self,T=matrix(np.identity(4)), radius = 10.0, color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,1.0),vRange=(0.0,2.0*pi),uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius
        
    #Name: parametricCircle.getPoint
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: return the equation of a parametric plane in a 4x4 matrix 
    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0, 0, self.__radius*u*cos(v))
        P.set(1, 0, self.__radius*u*sin(v))
        P.set(2, 0, 0)
        P.set(3, 0, 1)
        return P

    #Name: parametricCircle.setRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the radius of the circle 
    def setRadius(self, radius):
        self.__radius = radius

    #Name: parametricCircle.getRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: get the radius of the circle    
    def getRadius(self):
        return self.__radius



    