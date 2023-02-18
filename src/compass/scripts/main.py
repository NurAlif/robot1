#!/usr/bin/env python
import rospy
import serial
from utils.msg import compass

ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)

def talker():
    pub = rospy.Publisher('chattercompass', compass, queue_size=10)
    rospy.init_node('main', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        comps = compass()

        cc=str(ser.readline())
        if(len(cc) <= 0): continue

        mag = cc.split(':')

        comps.x = float(mag[0])
        comps.x = float(mag[1])
        comps.y = float(mag[2])
        pub.publish(comps)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
