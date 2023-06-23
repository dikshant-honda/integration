#! /usr/bin/env python3

import rospy
from perception.code.tests.extract_lane_3d import perception_lane_info
from perception.code.tests.extract_traffic_3d import traffic_info


lanes = perception_lane_info()
traffic = traffic_info()
print(lanes.image)