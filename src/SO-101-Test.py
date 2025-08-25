import torch
import os
from pathlib import Path

from lerobot.policies.pi0fast import Pi0FastPolicy

from lerobot.robots.so101_follower import SO101Follower
from lerobot.cameras.opencv import OpenCVCamera
from lerobot.cameras.realsense import RealSenseCamera
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.train import train

def main():
    robot = SO101Follower()
    camera = RealSenseCamera()
    dataset = LeRobotDataset()

    train(robot, camera, dataset)

if __name__ == "__main__":
    main()