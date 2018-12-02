#!/usr/bin/env python
'''
Author: Monica Lin
Date: 2018/12/01
Last update: 2018/12/01
Using opencv open webcam (not usb webcam)
    Input:  NC
    Output: Compress Image
'''
import rospy
import numpy as np
import os
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class OpencvWebcamNode(object):
    def __init__(self):
        self.node_name = rospy.get_name()
        rospy.loginfo("[%s] Initializing " %(self.node_name))

        self.verbose = True

        #self.width = 640
        #self.height = 480
        #self.fps = 60

        self.cv_bridge = CvBridge()
        #image_message = cv2_to_imgmsg(cv_image, encoding="passthrough")

        # Subscriber

        # Publisher
        rospy.Publisher
        self.pub_img = rospy.Publisher("~compressed", Image, queue_size=1)

        self.open_webcam()

    def initial_cam_info(self):
        #------- Pixel-to-Ray conversion variables
        self.fx = 930.6648
        self.fy = 937.2203
        self.cx = 650.7379
        self.cy = 367.3170
        self.k1 = 0.0697043
        self.k2 = 0.07730369
        self.p1 = 0.00000
        self.p2 = 0.00000
        self.k3 = 0.00000

    def open_webcam(self):
        self.cap = cv2.VideoCapture(0)
        if (self.cap.isOpened() == False):
        	print 'Capture failed to open'
        else:
            if(self.verbose): print 'Capture open image'
            ret, img = self.cap.read()
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)
            self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            self.heitht = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            print self.fps, self,width, self.heitht
            self.image_show(img)
            #cap.release()

    def image_show(self, img):
        cv2.imshow('webcam', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def read_image(self, path):
        img = cv2.imread(path,0)
        cv2.imshow(path,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def testing():
        print 'testing...'
        #self.read_image('test.jpeg')

    def on_shutdown(self):
        self.cap.release()
        cv2.destroyAllWindows()

        rospy.loginfo("[%s] Shutdown " %(self.node_name))

if __name__ == '__main__':
    rospy.init_node('opencv_webcam_node',anonymous=False)
    opencv_webcam_node = OpencvWebcamNode()
    rospy.on_shutdown(opencv_webcam_node.on_shutdown)
    rospy.spin()
