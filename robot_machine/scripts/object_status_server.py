#! /usr/bin/env python 


import rospy
from robot_machine.srv import*


def handle_bad_objects_status(req):
  print "Returning objects status code"
  return req.camera_a or req.camera_b    	



def bad_objects_status_server():
  rospy.init_node('bad_objects_status_server')
  m = rospy.Service('bad_objects_status' badObjectStatus, handle_bad_objects_status)
  print "ready to compute Bad object status"
  rospy.Spin()

if __name__ == 'main':
  bad_objects_status_server()
