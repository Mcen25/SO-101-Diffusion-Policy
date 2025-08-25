import torch
import os
from pathlib import Path

from lerobot.policies.diffusion import DiffusionPolicy
from lerobot.robots.so101_follower import SO101Follower
from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.scripts.train import train

def train_cube_pickup_policy():

    config = {
        "dataset": {
            "repo_id": "${HF_USER}/so101_cube_pickup_dataset",
            "split": "train"
        },
        "policy": {
            "type": "diffusion",
            "horizon": 16,
            "n_obs_steps": 2,
            "n_action_steps": 8,
            "device": "cuda" if torch.cuda.is_available() else "cpu"
        },
        "training": {
            "batch_size": 64,
            "learning_rate": 1e-4,
            "num_epochs": 2000,
            "save_freq": 100
        },
        "output_dir": "outputs/train/diffusion_so101_cube_pickup",
        "job_name": "diffusion_so101_cube_pickup",
        "wandb": {"enable": True}
    }

    dataset = LeRobotDataset(config["dataset"]["repo_id"])
    
    policy = DiffusionPolicy(
        config=config["policy"],
        dataset_stats=dataset.stats
    )
    
    train(
        policy=policy,
        dataset=dataset,
        config=config
    )
    
    print("Training completed!")

if __name__ == "__main__":
    train_cube_pickup_policy()