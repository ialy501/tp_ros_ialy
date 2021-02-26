#!/usr/bin/env python3


import rospy

from geometry_msgs.msg import PoseStamped
import numpy as np
import math

def talker():
	pub = rospy.Publisher('topic_pub', PoseStamped, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(15) # 15hz
	msg = PoseStamped()
	print(msg)
	msg.header.frame_id="map"
	t = - math.pi
	while not rospy.is_shutdown():
		#rayon = 0.5
		while t <=  math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(msg.pose.position.x)
			t = t + 0.1
			#hello_str = "hello world %s" % rospy.get_time()
			#rospy.loginfo(hello_str)
			pub.publish(msg)
			rate.sleep()
			
		while t >=  -math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			t = t - 0.1
			#hello_str = "hello world %s" % rospy.get_time()
			#rospy.loginfo(hello_str)
			pub.publish(msg)
			rate.sleep()


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
