import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import sys

CWD = os.getcwd()
IMG_DIR = CWD + '/img/'
SAVE_IM_DIR = CWD + '/lab4_cam/src'
sys.path.insert(0, SAVE_IM_DIR)

# import save_image as s
import save_webcam_img as cam_to_img 
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
img, save_name = cam_to_img.main()

#Step 2
#TODO: preprocessing... do if needed, but for rn median filtering + blurring works fine

#Step 3
canny_img = im_2_can.main(save_name)

# #Step 4
d.main(canny_img)

