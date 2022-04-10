#!/usr/bin/env python3
# license removed for brevity

#!/usr/bin/env python3
import rospy
from home_work.msg import Custom
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import Twist

w = [0,0]
wt = [0,0]
b = 0

def callback(data):
    global wt
    #ospy.loginfo(data.linear.x, data.angular.z)
    wt[0] = data.linear.x
    wt[1] = data.angular.z

def talker():
    pub = rospy.Publisher('custom_chatter', Custom)
    pub2 = rospy.Publisher('pose', Pose2D)
    rospy.init_node('custom_talker', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    r = rospy.Rate(10) #10hz
    msg = Custom()
    pos = Pose2D()
    

    while not rospy.is_shutdown():
        dt = rospy.Time.now().nsecs - msg.head.stamp.nsecs
        rospy.loginfo(dt)
        b = dt/(1+dt)
        global w, wt
        w[0] = b*w[0]+(1-b)*wt[0]
        w[1] = b*w[1]+(1-b)*wt[1]
        msg.head.stamp = rospy.Time.now()
        msg.left_en = int(w[0]*10**8)
        msg.right_en = int(w[1]*10**8)
        rospy.loginfo(msg)
        pub.publish(msg)
        pub2.publish(pos)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass


