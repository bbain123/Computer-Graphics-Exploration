import operator
from PIL import Image

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def drawPoint(self,point,color):
        if 0 <= point[0] < self.__width and 0 <= point[1] < self.__height:
            self.__image[point[0],point[1]] = color

    def drawLineNegative(self, point1, point2, color): #function for cases with slopes in between 0 and -1
        dx = point2.get(0,0) - point1.get(0,0)
        dy = point2.get(1,0) - point1.get(1,0)
        yi = 1
        if dy < 0:                              #check if y is increasing or decreasing
            yi = -1
            dy = dy * -1
        pi = 2*dy - dx

        y = point1.get(1,0)
        for x in range (int(point1.get(0,0)), int(point2.get(0,0))): #Bresenhams integer algorithm
            point = (x, y)
            self.drawPoint(point, color)
            if pi > 0:
                y = y + yi
                pi = pi + 2*(dy - dx)
            else:
                pi = pi + 2*dy

    def drawLinePositive(self, point1, point2, color): #function for cases with slopes greater than or equal to 1
        dx = point2.get(0,0) - point1.get(0,0)
        dy = point2.get(1,0) - point1.get(1,0)
        xi = 1
        if dx < 0:                          #check if x is increasing or decreasing
            xi = -1
            dx = dx*-1
        pi = 2*dx - dy

        x = point1.get(0,0)
        for y in range(int(point1.get(1,0)), int(point2.get(1,0))): #Bresenhams integer algorithm
            point = (x, y)
            self.drawPoint(point, color)
            if pi > 0:
                x = x + xi
                pi = pi + 2*(dx - dy)
            else:
                pi = pi + 2*dx


    def drawLine(self,point1,point2,color): #deals with all cases of slopes
        if abs(point2.get(1,0) - point1.get(1,0)) < abs(point2.get(0,0) - point1.get(0,0)): #dx is larger than dy
            if point1.get(0,0) > point2.get(0,0): #x1 is bigger than x2
                self.drawLineNegative(point2, point1, color) #smaller point p2 in first position
            else:
                self.drawLineNegative(point1, point2, color) #smaller point p1 in first position

        else:                                           #dy is larger than dx
            if point1.get(1,0) > point2.get(1,0):       #y1 is bigger than y2
                self.drawLinePositive(point2, point1, color) #smaller point p2 first
            else:                                        #y2 is bigger
                self.drawLinePositive(point1, point2, color) #smaller point p1 first


        

    


    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    def showImage(self):
        self.__canvas.show()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height