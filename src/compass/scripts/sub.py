#!/usr/bin/env python
import rospy
from utils.msg import compass

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %.1f", data.y)
    
def listener():

  
    rospy.init_node('sub', anonymous=True)

    rospy.Subscriber("chattercompass", compass, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
