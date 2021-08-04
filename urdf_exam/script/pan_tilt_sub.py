#!/usr/bin/env python 

import rospy
from sensor_msgs.msg import JointState

def foo_():

    rospy.init_node("move_pan_tilt")
    print(1)

if __name__ == "__main__":

    try:
        foo_()
    except rospy.ROSInterruptException():
        pass