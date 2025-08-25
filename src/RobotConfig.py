import torch
import os
from pathlib import Path

from lerobot.policies.diffusion import DiffusionPolicy
from lerobot.robots.so101_follower import SO101Follower
from lerobot.robots.so101_leader import SO101Leader
from lerobot.cameras.opencv import OpenCVCamera
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.train import train
from lerobot.scripts.record import record

def setup_robot_config():
    """Configure the SO-101 robot with cameras"""
    camera_config = {
        "front": {
            "type": "opencv", 
            "index_or_path": "0", 
            "width": 640, 
            "height": 480, 
            "fps": 30
        }
    }
    
    robot_config = {
        "type": "so101_follower",
        "port": "/dev/ttyACM0",
        "id": "matt_follower_arm",
        "cameras": camera_config
    }
    
    return robot_config

def main():
    robot_config = setup_robot_config()

    robot = SO101Follower(robot_config)
    
    leader_config = {
        "type": "so101_leader", 
        "port": "/dev/ttyACM1",
        "id": "matt_leader_arm"
    }
    leader = SO101Leader(leader_config)
    
    print("Robot setup complete!")

if __name__ == "__main__":
    main()