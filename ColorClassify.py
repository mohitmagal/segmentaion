import cv2
import numpy as np

class ColorClassify():
	def __init__(self):
		self.threshold = 20
	def __thresholdImage(self,img):
                imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
                ret,thresh1 = cv2.threshold(imgGray,self.threshold,255,cv2.THRESH_BINARY)
                return thresh1
	def classify(self,image):
		imgNew = self.__thresholdImage(image)
		unique, counts = np.unique(imgNew, return_counts=True)
		c = dict(zip(unique, counts))
		if (255 not in c):
			return 'white'
		elif (0 not in c):
			return 'black'
		elif c[255]>c[0]:
			return 'black'
		else:
			return 'white'
