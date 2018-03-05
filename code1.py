from Thresholding import Thresholding
from Main import Main

IMG_WIDTH = 128
IMG_HEIGHT = 128
IMG_CHANNELS = 3

TRAIN_PATH = '../stage1_train'
TEST_PATH = '../stage1_test'


Main().process(TRAIN_PATH,'testOutPut',"out.csv")
#Main().process(TEST_PATH,'testOutPut',"out1.csv")
