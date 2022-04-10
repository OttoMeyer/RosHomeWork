#!/usr/bin/env python3
from math import sin
from math import cos
import rospy
from home_work.msg import Custom
from geometry_msgs.msg import Pose2D


wl = 0
wr = 0
def callback(data):
    rospy.loginfo(data)
    wl = int(data.left_en)
    wr = int(data.right_en)

def callback2(data):
    rospy.loginfo(data)

def listener():
    r = 0.33
    L = 2.87
    O = 0
    x = 0
    y = 0
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("custom_chatter", Custom, callback)
    rospy.Subscriber("pose", Pose2D, callback2)
    while not rospy.is_shutdown():
        global wl, wr
        V = (r/2)*(wl+wr)
        Omega = (r/L)*(wr-wl)
        O += Omega
        x += V * cos(O)
        y += V * sin(O)
        #rospy.loginfo((x,y))

    # spin() simply keeps python from exiting until this node is stopped
    #rospy.spin()

if __name__ == '__main__':
    listener()