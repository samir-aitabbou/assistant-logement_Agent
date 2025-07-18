# utils/device.py
import torch

def detect_device():
    if torch.cuda.is_available():
        return 'cuda'
    return 'cpu'