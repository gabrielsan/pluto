#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String
import std_srvs.srv

def odrv_status_cb(data):
    rospy.loginfo(rospy.get_caller_id() + " ODrive status received: %s", data.data)
    calibrate_handle = rospy.ServiceProxy('/odrive/calibrate_motors', std_srvs.srv.Trigger)

    if (data.data == "connected"):
        rospy.loginfo("calling calibration")
        res = calibrate_handle()
        rospy.loginfo("calibrate res: %d %s", res.success, res.message)
    else:
        rospy.loginfo("nothing to do")

def monitor():
    #
    rospy.loginfo("Waiting for /odrive/calibrate_motors service to be available")
    rospy.wait_for_service('/odrive/calibrate_motors')
    rospy.loginfo("/odrive/calibrate_motors service is available now")

    rospy.loginfo("Starting node")
    rospy.init_node("odrv_monitor", anonymous=True)

    rospy.loginfo("Subscribing to topic /odrive/status")
    rospy.Subscriber("/odrive/status", String, odrv_status_cb)

    rospy.loginfo("Waiting for status messages from now on")
    rospy.spin()

if __name__ == '__main__':
    try:
        monitor()
    except rospy.ROSInterruptException:
        pass

