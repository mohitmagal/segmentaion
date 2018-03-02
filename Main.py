import os,cv2
from ColorClassify import ColorClassify
from Thresholding import Thresholding
from MakeContour import MakeContour

class Main():
	def __init__(self):
		pass
	def process(self,inputPath,processFolder):
		directories = os.listdir(inputPath)
		for dr in directories:
			path = os.path.join(inputPath,dr)
			path = os.path.join(path,'images')
			files = os.listdir(path)
			for f in files:
				fPath = os.path.join(path,f)
				img = cv2.imread(fPath)
				imgType = ColorClassify().classify(img)
				imgNew = Thresholding().thresholdImage(fPath,imgType)
				cv2.imwrite(os.path.join(processFolder,f+imgType+".png"),img)
				if imgType=="black":
                                        imgNew = 255-imgNew
				tmpPath = os.path.join("/tmp",f)
				cv2.imwrite(tmpPath,imgNew)
				imgNew = MakeContour().contours(tmpPath)
				os.system("sudo rm \""+tmpPath+"\"")
				cv2.imwrite(os.path.join(processFolder,f),imgNew)
				break
