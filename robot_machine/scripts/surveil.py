

import rospy
from std_msgs.msg import Bool

def callback_str(data):
  rospy.loginfo(data.data)

def conveyor_listener():
  rospy.init_node('Conveyer_status', anonymous = True)
  rospy.Subscriber('conveyor_status', Bool, callback_str)
  rospy.Spin()

if __name__ == 'main':
  conveyor_listener()
