#!/usr/bin/env python 

import rospy
from sensor_msgs.msg import JointState

def pub_pan_tilt():
    
    rospy.init_node("move_pan_tilt",anonymous=True)
    pt_pub= rospy.Publisher("/joint_states",JointState,queue_size=10)

    pt_vel=JointState()
    rate=rospy.Rate(10)

    while not rospy.is_shutdown():
        pt_vel.position = [1.3 , -3.14]
        rospy.loginfo(pt_vel.position)
        pt_pub.publish(pt_vel)
        rate.sleep()


if __name__=="__main__":
    
    try:
        pub_pan_tilt()
    except rospy.ROSInterruptException:
        pass
