#! /usr/bin/env python 

import rospy
from std_msgs.msg import Bool

def conveyor_surveil():
  hello_pub = rospy.Publisher('conveyor_status', Bool, queue_size=10)
  rospy.init_node('Cameras', anonymous = True)
  rate = rospy.Rate(10)
  while not rospy.is_shutdown(): 
    camera_a = True
    camera_b = False
    greeting = camera_a or camera_b
    rospy.loginfo(greeting)
    hello_pub.publish(greeting)
    rate.sleep()


if __name__ == 'main':
  try:
    conveyor_surveil()
  except rospy.ROSInterruptException:
    pass

