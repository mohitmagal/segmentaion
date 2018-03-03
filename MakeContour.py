import cv2,os
import numpy as np
from RunEncode import RunEncode

class MakeContour():
	def __init__(self):
		pass
	def contours(self,img):
		path = img
		img = cv2.imread(img)
		img1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
		thresh,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
		contours, hierarchy = cv2.findContours(img1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		runEncodeOutput = []
		for i in xrange(0,len(contours)):
			cnt = contours[i]
			if int(hierarchy[0,i,3])==-1:
				hull = cv2.convexHull(cnt)
				tempImg = np.zeros(img.shape, np.uint8)
				cv2.drawContours(tempImg,[cnt],0,(255,255,255),-1)
				#cv2.drawContours(tempImg,[hull],0,(255,255,255),-1)
				tempImg = cv2.cvtColor(tempImg,cv2.COLOR_BGR2GRAY)
				thresh,tempImg = cv2.threshold(tempImg,127,255,cv2.THRESH_BINARY)
				y,x = np.where(tempImg==255)
				if int(y.shape[0])<15:
					continue
				string = RunEncode().getOutput(tempImg,255)
				runEncodeOutput += [[os.path.basename(path).split('.')[0],string]]
				cv2.drawContours(img,[hull],0,(0,0,255),2)
				cv2.drawContours(img,[cnt],0,(0,255,0),1)
		return img,runEncodeOutput
