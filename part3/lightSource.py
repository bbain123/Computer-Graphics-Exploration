import numpy as np
from matrix import matrix

class lightSource:

    #Name: lightSource.__init__
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: To initialize posistion matrix, color, and intensity of light source
    def __init__(self,position=matrix(np.zeros((4,1))),color=(0,0,0),intensity=(1.0,1.0,1.0)):
        self.__position = position
        self.__color = color
        self.__intensity = intensity

    #Name: lightSource.getPosition
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: returns position matrix of light source
    def getPosition(self):
        return self.__position

    #Name: lightSource.getColor
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: returns the color tuple of the light source
    def getColor(self):
        return self.__color

    #Name: lightSource.getIntensity
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: returns the intensity of the light source as a tuple (R, G, B intensities)
    def getIntensity(self):
        return self.__intensity

    #Name: lightSource.setPosition
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: sets light source position matrix
    def setPosition(self,position):
        self.__position = position

    #Name: lightSource.setColor
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: sets light source color tuple
    def setColor(self,color):
        self.__color = color

    #Name: lightSource.setIntensity
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: sets light source intensity tuple
    def setIntensity(self,intensity):
        self.__intensity = intensity
