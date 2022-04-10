#!/usr/bin/env python3
import rospy

from geometry_msgs.msg import Twist



def talker():
    pub = rospy.Publisher('custom_twist', Twist)
    rospy.init_node('custom_twister', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Twist()
    msg.linear.x = 10
    msg.linear.y = 5
    msg.linear.z = 0
    msg.angular.x = 10
    

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass