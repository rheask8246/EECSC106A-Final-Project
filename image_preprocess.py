import matplotlib.pyplot as plt 
import numpy as np 
from skimage import io  
import os
from skimage.filters.rank import entropy 
from skimage.morphology import disk 
from skimage.color import rgb2gray 
import cv2

this_file = os.getcwd()
IMG_DIR = this_file + '/img/'

if __name__ == "__main__":
    #showing raw image
    img_path = IMG_DIR + "heath.jpg"
    image = io.imread(img_path) 
    # plt.ion()
    plt.axis('off') # turn off axis labels 
    plt.title("Raw Image")
    plt.imshow(image) 
    plt.show()

    # make_entropy_img = input("Press 'Enter' to show entropy image.")
    # if make_entropy_img == '':
    gray_image = rgb2gray(image) 
    entropy_image = entropy(gray_image, disk(7))  
    plt.axis('off')
    plt.imshow(entropy_image)
    plt.show()

    max_img = entropy_image.max()
    scale = 255/max_img
    entropy_image = scale*entropy_image
    plt.axis('off')
    plt.imshow(entropy_image)
    plt.show()

    cv2.imwrite(IMG_DIR + "heath_entropy.jpg", entropy_image)