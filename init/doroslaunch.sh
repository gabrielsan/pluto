#!/bin/bash
source /opt/ros/kinetic/setup.bash
. ~/catkin_ws/devel/setup.bash
export ROS_HOSTNAME=pluto.local

exec roslaunch pluto pluto.launch
