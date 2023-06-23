#! /usr/bin/env python3

import rospy
from perception.code.tests.extract_lane_3d import perception_lane_info

info = perception_lane_info()

print(info.image)