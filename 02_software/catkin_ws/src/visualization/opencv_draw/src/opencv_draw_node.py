#!/usr/bin/env python

import rospy
import numpy as numpy
import cv2 as cv

class OpencvDraw(object):
    def __init__ (self):
        self.node_name = rospy.get_name()

        # Parameters
        self.msg_name = 'haha'
        self.image_name =

        # Publisher

        # Subscriber


if __name__ == "__main__":
    rospy.init_node('opencv_draw_node', anonymous=False)
    opencv_draw_node = OpencvDraw()

    rospy.spin()
