#!/bin/bash

# SO Arm 101 Setup Script for LeRobot
echo "Setting up SO Arm 101 project with LeRobot..."

# Check if conda environment exists
if conda env list | grep -q "lerobot"; then
    echo "✓ Found existing 'lerobot' conda environment"
    source activate lerobot
else
    echo "❌ 'lerobot' conda environment not found"
    echo "Please create it first with: conda create -n lerobot python=3.10"
    exit 1
fi

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Check if LeRobot is installed
python -c "import lerobot" 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ LeRobot is installed"
else
    echo "Installing LeRobot..."
    # Install LeRobot from source
    git clone https://github.com/huggingface/lerobot.git /tmp/lerobot
    cd /tmp/lerobot
    pip install -e .
    cd -
fi

# Create necessary directories
echo "Creating project directories..."
mkdir -p data/raw
mkdir -p data/processed
mkdir -p models
mkdir -p logs
mkdir -p outputs

# Set up git hooks (optional)
echo "Setting up project..."

# Make scripts executable
chmod +x scripts/*.py

echo "✅ Setup completed!"
echo ""
echo "Next steps:"
echo "1. Configure your robot connection in config/config.yaml"
echo "2. Test robot connection: python scripts/test_robot.py"
echo "3. Collect data: python scripts/collect_data.py"
echo "4. Train policy: python scripts/train_policy.py"
echo "5. Deploy policy: python scripts/deploy_policy.py"
