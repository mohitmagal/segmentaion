import cv2,os
from ColorClassify import ColorClassify
import numpy as np

class Thresholding():
        def __init__(self):
		pass
        def thresholdImage(self,image,imgType):
                img = cv2.imread(image)
                imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
		if imgType=="white":
			'''y,x = np.where(imgGray<20)
			for i in xrange(0,int(y.shape[0])):
				imgGray[int(y[i])][int(x[i])] = 0'''
			#ret,imgGray = cv2.threshold(imgGray,20,255,cv2.THRESH_BINARY)
			ret,imgGray = cv2.threshold(imgGray,30,255,cv2.THRESH_BINARY)
		elif imgType=="black":
			'''y,x = np.where(imgGray>120)
			for i in xrange(0,int(y.shape[0])):
				imgGray[int(y[i])][int(x[i])] = 255'''
			ret,imgGray = cv2.threshold(imgGray,120,255,cv2.THRESH_BINARY)
                return imgGray
	def errorFix(self,img):
		rows,cols = img.shape
		whiteCount = 0
		blackCount = 0
		for i in xrange(0,rows):
			if int(img[i,0])==0:
				blackCount += 1
			elif int(img[i,0])==255:
				whiteCount += 1
			if int(img[i,cols-1])==0:
				blackCount += 1
			elif int(img[i,cols-1])==255:
				whiteCount += 1
		for i in xrange(0,cols):
			if int(img[0,i])==0:
				blackCount += 1
			elif int(img[0,i])==255:
				whiteCount += 1
			if int(img[rows-1,i])==0:
                                blackCount += 1
                        elif int(img[rows-1,i])==255:
                                whiteCount += 1
		if whiteCount>blackCount:
			return True
		else:
			return False
