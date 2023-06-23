#! /usr/bin/env python3

import rospy
import numpy as np
import argparse
from perception.code.tests.extract_lane_3d import perception_lane_info
from perception.code.test_td_net import Load


# lane information
lanes = perception_lane_info()

# traffic information
load_traffic_data = Load()
traffic_coords = Load.run()


# perception loop
class perception:
    def __init__(self) -> None:
        # Load the camera matrix and distortion coefficients obtained from calibration
        self.camera_matrix = np.load('camera_matrix.npy')
        self.dist_coeffs = np.load('dist_coeffs.npy')

# load the arguments
class args:
    def __init__(self) -> None:
        pass

    def parse_opt(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--source', type=str, help='file/dir')
        self.parser.add_argument('--yolo', default=5, type=int, help='Choose YOLO version [4, 5, 7]. (Default is 5)')
        self.parser.add_argument('--root', default='YOLOv5', type=str, help='Choose detector\'s root folder (e.g. C:/YOLOv5). (Default is the current path)')
        self.parser.add_argument('--save', default='results', type=str, help='Choose address folder for saving results')
        self.parser.add_argument('--start', default=0, type=int, help='Start frame')
        self.parser.add_argument('--end', default=-1, type=int, help='End frame')
        self.parser.add_argument('--weights', default='yolov5l.pt', type=str, help='Address of trained weights. (Default is [yolov5l.pt])')
        self.parser.add_argument('--cfg', default=None, type=str, help='Address of YOLOv4 network architecture. (Default is [./cfg/yolov4.cgf])')
        self.parser.add_argument('--data', default=None, type=str, help='Address of YOLOv4 trained model data. (Default is [./cfg/coco.data]')
        opt = self.parser.parse_args()
        return opt

# main function
if __name__ == "__main__":
    # parsed arguments
    opt = args.parse_opt()

    # run the pretest
