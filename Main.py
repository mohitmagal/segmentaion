import os,cv2,csv
from tqdm import tqdm
from ColorClassify import ColorClassify
from Thresholding import Thresholding
from MakeContour import MakeContour

class Main():
	def __init__(self):
		pass
	def process(self,inputPath,processFolder,outputFile):
		fp = open(outputFile,"w")
		writer = csv.writer(fp)
		writer.writerow(['ImageId','EncodedPixels'])
		directories = os.listdir(inputPath)
		for dr in tqdm(directories):
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
				if Thresholding().errorFix(imgNew):
					imgNew = 255-imgNew
				tmpPath = os.path.join("/tmp",f)
				cv2.imwrite(tmpPath,imgNew)
				imgNew,runEncodeOutput = MakeContour().contours(tmpPath)
				os.system("sudo rm \""+tmpPath+"\"")
				cv2.imwrite(os.path.join(processFolder,f),imgNew)
				for row in runEncodeOutput:
					writer.writerow(row)
		fp.close()
