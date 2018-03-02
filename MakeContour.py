import cv2
import numpy as np
from copy import deepcopy
from pprint import pprint

class MakeContour():
	def __init__(self):
		pass
	def contours(self,img):
		img = cv2.imread(img)
		img1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
		thresh,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
		im2, contours, hierarchy = cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		for i in xrange(0,len(contours)):
			cnt = contours[i]
			if int(hierarchy[0,i,3])==-1:
				hull = cv2.convexHull(cnt)
				cv2.drawContours(img,[hull],0,(0,0,255),2)
				cv2.drawContours(img,[cnt],0,(0,255,0),1)
		return img
