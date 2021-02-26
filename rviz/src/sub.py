#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped
import numpy as np
import math


def callback(data):
	print(data)
	pub = rospy.Publisher('topic_pub', PoseStamped, queue_size=10)
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
			if data.data == True :
				t = t + 0.1
				pub.publish(msg)
				rate.sleep()
				break				
			
			elif data.data == False :
				t = t
				pub.publish(msg)
				rate.sleep()
				break				
				

			
		while t >=  -math.pi :	    
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			if data.data == True :
				t = t + 0.1
				pub.publish(msg)
				rate.sleep()
				break				
			
			elif data.data == False :
				t = t
				pub.publish(msg)
				rate.sleep()
				break	
		
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("button_state", Bool , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
	try:
		listener()
	except rospy.ROSInterruptException:
		pass
