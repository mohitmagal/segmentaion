import cv2
import numpy as np
from itertools  import groupby

class RunEncode():
	def __init__(self):
		pass
	def getOutput(self,image,colorValue):
		try:
			r,c,dim = image.shape
			if dim!=1:
				image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
				thresh,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
		except:
			pass
		flattenImage = image.flatten('F')
		flattenImage = flattenImage.tolist()
		groupedFlattenImage = groupby(flattenImage)
		count = 0
		encoded = ""
		for elem in groupedFlattenImage:
			a = list(elem[1])
			if elem[0]==colorValue:
				encoded = encoded+" "+str(count+1)+" "+str(len(a))
			count += len(a)
		encoded = encoded.strip()
		return encoded
'''
image = cv2.imread("../stage1_train/00071198d059ba7f5914a526d124d28e6d010c92466da21d4a04cd5413362552/masks/07a9bf1d7594af2763c86e93f05d22c4d5181353c6d3ab30a345b908ffe5aadc.png")
#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
print RunEncode().getOutput(image,255)'''
