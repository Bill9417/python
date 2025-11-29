import subprocess

def has_cuda():
    # Method 1: PyTorch
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        pass

    # Method 2: nvidia-smi
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False

def detect_device():
    return "cuda" if has_cuda() else "ml"

if __name__ == "__main__":
    print(detect_device())
