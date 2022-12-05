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
    # gray_image = rgb2gray(image) 
    # entropy_image = entropy(gray_image, disk(7))  
    # plt.axis('off')
    # plt.imshow(entropy_image)
    # plt.show()

    # max_img = entropy_image.max()
    # scale = 255/max_img
    # entropy_image = scale*entropy_image
    # plt.axis('off')
    # plt.imshow(entropy_image)
    # plt.show()

    # cv2.imwrite(IMG_DIR + "heath_entropy.jpg", entropy_image)



    #try to recognize a face
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    print("[INFO] Found {0} Faces.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]
        print("[INFO] Object found. Saving locally.")
        plt.axis('off') # turn off axis labels 
        plt.imshow(roi_color) 
        plt.show()
        cv2.imwrite(IMG_DIR + 'heath_preprocess.jpg', roi_color)

    status = cv2.imwrite(IMG_DIR + "heath_cutout.jpg", image)
    print("[INFO] Image written to filesystem: ", status)