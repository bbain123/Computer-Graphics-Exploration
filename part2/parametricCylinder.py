from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

class parametricCylinder(parametricObject):

    #Name: parametricCylinder.__init__
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: Initialize all objects of type parametricCylinder
    def __init__(self,T=matrix(np.identity(4)), height = 10.0, radius = 5.0, color=(255,255,255),reflectance=(0.2,0.4,0.4,1.0),uRange=(0.0,1.0),vRange=(0.0,2.0*pi),uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T,color,reflectance,uRange,vRange,uvDelta)
        self.__radius = radius
        self.__height = height
        
    #Name: parametricCylinder.getPoint
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: returns the equation of a parametric cylinder in a 4x4 matrix  
    def getPoint(self,u,v):
        P = matrix(np.ones((4,1)))
        P.set(0, 0, self.__radius*sin(v))
        P.set(1, 0, self.__radius*cos(v))
        P.set(2, 0, self.__height*u)
        P.set(3, 0, 1)
        return P

    #Name: parametricCylinder.setRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the radius of the cylinder
    def setRadius(self, radius):
        self.__radius = radius

    #Name: parametricCylinder.getRadius
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the radius of the cylinder     
    def getRadius(self):
        return self.__radius

    #Name: parametricCylinder.setHeight
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: set the height of the cylinder 
    def setHeight(self, height):
        self.__radius = radius

    #Name: parametricCylinder.getHeight
    #Author: Brendan
    #Date of Creation: Feb 15, 2022
    #Purpose: return the height of the cylinder object    
    def getHeight(self):
        return self.__height

