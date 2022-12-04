import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

CWD = os.getcwd()
IMG_DIR = CWD + '/img/'
SAVE_IM_DIR = CWD + '/lab4_cam/src'
sys.path.insert(0, SAVE_IM_DIR)

import save_image as s
import image_to_canny as im_2_can
import draw as d

##########################################################
#Wrapper program. Runs:
#1. save_image.py #take image from webcam and save in /img folder.
#2 image_preprocess.py #isolate face in image.
#2. image_to_canny.py #take raw image and run canny edge detection with adjustable thresholds. save edge image in folder.
#4. draw.py #takes cleaned image and creates trajectory for saweyer to draw.
##########################################################


#Step 1
raw_img = s.main() #need to test if this works

#Step 2
#TODO: preprocess

#Step 3
canny_img = im_2_can.main(raw_img)

#Step 4
d.main(canny_img)

