import torch
from lerobot.policies.diffusion import DiffusionPolicy
from lerobot.robots.so101_follower import SO101Follower
from lerobot.cameras.opencv import OpenCVCamera
from lerobot.cameras.realsense import RealSenseCamera

def run_inference():
    
    policy = DiffusionPolicy.from_pretrained("${HF_USER}/diffusion_so101_cube_pickup_policy")
    
    robot = SO101Follower({
        "port": "/dev/ttyACM0",
        "id": "matt_follower_arm"
    })
    
    cameras = {
        "front": OpenCVCamera("0", width=640, height=480, fps=30),
    }
    
    for episode in range(10):
        print(f"Running episode {episode + 1}")
        
        robot.reset()
        
        observation = {}
        for camera_name, camera in cameras.items():
            observation[camera_name] = camera.read()
        
        observation.update(robot.get_observation())
        
        with torch.no_grad():
            action = policy.select_action(observation)
        
        robot.send_action(action)
        
        print(f"Episode {episode + 1} completed")

if __name__ == "__main__":
    run_inference()