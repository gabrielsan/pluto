#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def odrv_status_cb(data):
    rospy.loginfo(rospy.get_caller_id() + " ODrive status received: %s", data.data)

def monitor():
    #
    rospy.init_node("odrv_monitor", anonymous=True)

    rospy.Subscriber("/odrive/status", String, odrv_status_cb)

    rospy.spin()

if __name__ == '__main__':
    try:
        monitor()
    except rospy.ROSInterruptException:
        pass

