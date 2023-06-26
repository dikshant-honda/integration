#! /usr/bin/env python3

import rospy
import os
import numpy as np
import argparse
from perception.code.tests.extract_lane_3d import perception_lane_info
from perception.code.test_td_net import detect
from env_info.lane_info import LaneInfo 


# perception loop
class perception:
    def __init__(self) -> None:
        # Load the camera matrix and distortion coefficients obtained from calibration
        self.camera_matrix = np.load('camera_matrix.npy')
        self.dist_coeffs = np.load('dist_coeffs.npy')
    
    def info(self, path, opt):
        result = detect(path, opt).Run()
        return result
    
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

# pretest for arguments check
class run:
    def __init__(self) -> None:
        pass

    def load(self, opt):
        if opt.source:
            supSuffix =  ['mp4', 'avi', 'mpg', 'mov']
            if os.path.isdir(opt.source):  
                print("\nIt is a directory")
                if not os.path.exists(opt.source + '/Config'): print('Configuration Not Found!'); return 0
                for entry in os.scandir(opt.source):
                    if entry.is_file():
                        suffix = os.path.basename(entry.path).split('.')[1]
                        if suffix in supSuffix:
                            print(f">>>>> Start item : {entry.name}")
                            return entry.path, opt
                        else: print(f'Format not support for {os.path.basename(entry.path)}, supported formats are {supSuffix}')
            else:
                if os.path.exists(opt.source):
                    root = os.path.dirname(os.path.abspath(opt.source))
                    filename = os.path.basename(opt.source).split('.')[0]
                    paths = root + '/' + filename
                    if not os.path.exists(paths + '/config.json'): print('::: Configuration Not Found!'); return 0
                    suffix = os.path.basename(opt.source).split('.')[1]
                    if suffix in supSuffix:
                        print(f">>>>> Start item : {opt.source}")
                        return entry.path, opt
                    else: print(f'Format not support for {os.path.basename(opt.source)}, supported formats are {supSuffix}')                
                else: print(f'{opt.source} Not Found!')
        else: print('Use --source [file/folder]')        

# main function
if __name__ == "__main__":
    # parsed arguments
    arg = args()
    opt = arg.parse_opt()

    # run the pretest
    test = run()
    path, opt = test.load(opt)

    # lane information
    lanes = perception_lane_info()
    lane_info = lanes.lane_coordinates()

    # perception 
    perception_res = perception()
    traffic_info = perception_res.info(path, opt)

    test = LaneInfo()