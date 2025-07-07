# AIML Utilities for Linea

# Using PyTorch (CPU and GPU) for AI/ML tasks

import torch
import torch.nn as nn
from liblinea import Linea

class Basic:
    @staticmethod
    def isCUDA():
        if torch.cuda.is_available():
            Linea.display("CUDA is available")
            return True
        else:
            Linea.display("CUDA is not available")
            return False
        
    @staticmethod
    def initRandomTensor():
        tensor = torch.rand(3, 3)
        Linea.display(f"Initialized random tensor:\n{tensor}")
        return tensor