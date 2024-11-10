import numpy as np
from matrix import matrix

class tessel:

	#Name: tessel.__init__
    #Author: Brendan
    #Date of Creation: March 16, 2022
    #Purpose: Initialize all objects of tessel. Initialize and set the faceList list and facePoints list 
	def __init__(self,objectList,camera,light):
		EPSILON = 0.001
		self.__faceList = [] #Create an empty list of faces. This is an instance variable for this class
		facePoints = [] #Create an empty list for the points forming a face
		light.setPosition(camera.worldToViewingCoordinates(light.getPosition()))#Transform the position of the light into viewing coordinates (use method worldToViewingCoordinates from class cameraMatrix)
		red = light.getIntensity()[0] #Get light intensity values
		green = light.getIntensity()[1]
		blue = light.getIntensity()[2]


		for object in objectList:
			objectColor = object.getColor() #Get the object color
			u = object.getURange()[0] #u becomes the start value of the u-parameter range for the object
			
			while u + object.getUVDelta()[0] < object.getURange()[1] + EPSILON: #While u + the delta u of the object is smaller than the final value of the u-parameter range + EPSILON:
				v = object.getVRange()[0] #v become the start value of the v-parameter range for the object

				while v + object.getUVDelta()[1] < object.getVRange()[1] + EPSILON: #While v + the delta v of the object is smaller than the final value of the v-parameter range + EPSILON:
							#Collect surface points transformed into viewing coordinates in the following way:

					#Get object point at (u,v), (u, v + delta v), (u + delta u, v + delta v), and (u + delta u, v)
					p1 = object.getPoint(u, v)
					p2 = object.getPoint(u, v + object.getUVDelta()[1])
					p3 = object.getPoint(u + object.getUVDelta()[0], v + object.getUVDelta()[1])
					p4 = object.getPoint(u + object.getUVDelta()[0], v)
					#Transform these points with the transformation matrix of the object
					T = object.getT()
					p1 = T*p1
					p2 = T*p2
					p3 = T*p3
					p4 = T*p4
					#Transform these points from world to viewing coordinates
					p1 = camera.worldToViewingCoordinates(p1)
					p2 = camera.worldToViewingCoordinates(p2)
					p3 = camera.worldToViewingCoordinates(p3)
					p4 = camera.worldToViewingCoordinates(p4)
					#Append these points (respecting the order) to the list of face points
					facePoints.append(p1)
					facePoints.append(p2)
					facePoints.append(p3)
					facePoints.append(p4)
							#Make sure we don't render any face with one or more points behind the near plane in the following way:
					#Compute the minimum Z-coordinate from the face points
					minZ = self.__minCoordinate(facePoints, 2)

					if minZ < camera.getNp()*-1: #If this minimum Z-value is not greater than -(Near Plane) (so the face is not behind the near plane):
						centroidPoint = self.__centroid(facePoints) #Compute the centroid point of the face points
						faceNormal = self.__vectorNormal(facePoints) #Compute the normal vector of the face, normalized
						faceNormal = faceNormal.normalize()

					#Compute face shading, excluding back faces (normal vector pointing away from camera) in the following way:
					if not self.__backFace(centroidPoint, faceNormal):
						S = self.__vectorToLightSource(light.getPosition(), centroidPoint) #S is the vector from face centroid to light source, normalized
						S = S.normalize()
						#R is the vector of specular reflection
						R = self.__vectorSpecular(S, faceNormal)
						#V is the vector from the face centroid to the origin of viewing coordinates
						V = self.__vectorToEye(centroidPoint)
						#Compute color index
						index = self.__colorIndex(object, faceNormal, S, R, V)

						#Obtain face color (in the RGB 3-color channels, integer values) as a tuple:
						#(object color (red channel) * light intensity (red channel) * index,
						# object color (green channel) * light intensity (green channel) * index,
						# object color (blue channel) * light intensity (blue channel) * index)
						Red = objectColor[0] * red * index
						Green = objectColor[1] * green * index
						Blue = objectColor[2] * blue * index
						color = (int(Red), int(Green), int(Blue))

						#For each face point:
						#Transform point into 2D pixel coordinates and append to a pixel face point list
						pixelFacePoints = []
						pixelFacePoints.append(camera.viewingToPixelCoordinates(p1))
						pixelFacePoints.append(camera.viewingToPixelCoordinates(p2))
						pixelFacePoints.append(camera.viewingToPixelCoordinates(p3))
						pixelFacePoints.append(camera.viewingToPixelCoordinates(p4))

						#Add all face attributes to the list of faces in the following manner:
						#transform the face centroid from viewing to pixel coordinates
						centroidPoint = camera.viewingToPixelCoordinates(centroidPoint)
						zCoord = int(centroidPoint.get(2,0)) 
						#append pixel Z-coordinate of face centroid, the pixel face point list, and the face color
						attributeList = []
						attributeList.append(zCoord)
						attributeList.append(pixelFacePoints)
						attributeList.append(color)
						self.__faceList.append(attributeList)

					#Re-initialize the list of face points to empty
					facePoints = []
					v = v + object.getUVDelta()[1] #v become v + delta v
				u = u + object.getUVDelta()[0] #u becomes u + delta u

	#Name: tessel.minCoordinate
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Computes the minimum X, Y, or Z coordinate from a list of 3D points 
	def __minCoordinate(self,facePoints,coord): 
	#Coord = 0 indicates minimum X coord, 1 indicates minimum Y coord, 2 indicates minimum Z coord.
		min = facePoints[0].get(coord,0)
		for point in facePoints:
			if point.get(coord,0) < min:
				min = point.get(coord,0)
		return min

	#Name: tessel.backFace
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Computes if a face is a back face with using the dot product of the face centroid with the face normal vector
	def __backFace(self,C,N):
		return C.dotProduct(N) > 0.0


	#Name: tessel.centroid
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Computes the centroid point of a face by averaging the points of the face
	def __centroid(self,facePoints):
		sum = matrix(np.zeros((4,1)))
		for point in facePoints:
			sum += point
		return sum.scalarMultiply(1.0/float(len(facePoints)))

	#Name: tessel.vectorNormal
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Computes the normalized vector normal to a face with the cross product
	def __vectorNormal(self,facePoints):
		U = (facePoints[3] - facePoints[1]).removeRow(3).normalize()
		V = (facePoints[2] - facePoints[0]).removeRow(3).normalize()
		return U.crossProduct(V).normalize().insertRow(3,0.0)

	#Name: tessel.vectorToLightSource
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: computes a vector from a vector to the light source
	def __vectorToLightSource(self,L,C):
		return (L.removeRow(3) - C.removeRow(3)).normalize().insertRow(3,0.0)

	#Name: tessel.vectorSpecular
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: creates a vector of specular reflection
	def __vectorSpecular(self,S,N):
		return  S.scalarMultiply(-1.0) + N.scalarMultiply(2.0*(S.dotProduct(N)))

	#Name: tessel.vectorToEye
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Creates a vector from origin to viewing coordinates
	def __vectorToEye(self,C):
		return C.removeRow(3).scalarMultiply(-1.0).normalize().insertRow(3,0.0)

	#Name: tessel.colorIndex
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: Creates the total light intensity
	def __colorIndex(self,object,N,S,R,V):
	#Computes local components of shading
		Id = max(N.dotProduct(S),0.0)
		Is = max(R.dotProduct(V),0.0)
		r = object.getReflectance()
		index = r[0] + r[1]*Id + r[2]*Is**r[3]
		return index

	#Name: tessel.centroid
    #Author: Dr. Davis
    #Date of Creation: March 16, 2022
    #Purpose: returns the list of faces
	def getFaceList(self):
		return self.__faceList