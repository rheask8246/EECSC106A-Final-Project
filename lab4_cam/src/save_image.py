#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from lab4_cam.srv import ImageSrv, ImageSrvResponse
import cv2, time, sys
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import os

this_file = os.getcwd()
IMG_DIR = this_file + '/img/'
# Create a CvBridge to convert ROS messages to OpenCV images
bridge = CvBridge()

# Converts a ROS Image message to a NumPy array to be displayed by OpenCV
def ros_to_np_img(ros_img_msg):
  try:
    cv2_img = bridge.imgmsg_to_cv2(ros_img_msg,'bgr8')
  except CvBridgeError as e:
    print(e)
  else:

    img_name = input("Save image as: ")
    cwd = os.getcwd()
    cv2.imwrite(IMG_DIR + img_name + '.jpg', cv2_img)
    print("Saved image", img_name)
    return np.array(cv2_img), img_name

def main():
  
  # Waits for the image service to become available
  rospy.wait_for_service('last_image')
  
  # Initializes the image processing node
  rospy.init_node('save_image_node')
  
  # Creates a function used to call the 
  # image capture service: ImageSrv is the service type
  last_image_service = rospy.ServiceProxy('last_image', ImageSrv)
    
    
  take_image = input('Press enter to capture an image:')
  if take_image == '':
    # Request the last image from the image service
    # And extract the ROS Image from the ImageSrv service
    # Remember that ImageSrv.image_data was
    # defined to be of type sensor_msgs.msg.Image
    ros_img_msg = last_image_service().image_data

    # Convert the ROS message to a NumPy image
    np_image, img_name = ros_to_np_img(ros_img_msg)
    print("created np image")
    # rospy.signal_shutdown("Shutting down.")

    # # Display the CV Image
    # cv2.imshow("CV Image", np_image)

    # # Loop until the user presses a key
    # key = -1
    # while key == -1:
    #   if rospy.is_shutdown():
    #     raise KeyboardInterrupt
    #   key = cv2.waitKey(100)
    
    # # When done, get rid of windows
    # cv2.destroyAllWindows()
  return img_name

