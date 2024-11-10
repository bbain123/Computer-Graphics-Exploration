from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCone(parametricObject):

    #Name: parametricCone.__init__
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: Initialize all objects of type parametricCone 
    def __init__(self,T=matrix(np.identity(4)), height = 10.0, radius = 5.0, color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,1.0),vRange=(0.0,2.0*pi),uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius
        self.__height = height
        
    #Name: parametricCone.getPoint
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: returns the equation of a parametric cone in a 4x4 matrix  
    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0, 0, ((self.__height*(1 - u))/self.__height)*self.__radius*sin(v))
        P.set(1, 0, ((self.__height*(1 - u))/self.__height)*self.__radius*cos(v))
        P.set(2, 0, self.__height*u)
        P.set(3, 0, 1)
        return P

    #Name: parametricCone.setRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: sets the radius of the cone object 
    def setRadius(self, radius):
        self.__radius = radius

    #Name: parametricCone.setRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: returns the radius set for the cone      
    def getRadius(self):
        return self.__radius

    #Name: parametricCone.setHeight
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: sets the height of the cone  
    def setHeight(self, height):
        self.__radius = radius

    #Name: parametricCone.getHeight
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: returns the height of a parametric cone object
    def getHeight(self):
        return self.__height