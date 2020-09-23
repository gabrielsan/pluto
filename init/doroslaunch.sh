#!/bin/bash
source /opt/ros/melodic/setup.bash
source /home/pluto/pluto_ws/devel/setup.bash
export ROS_HOSTNAME=pluto.local

exec roslaunch pluto pluto.launch
