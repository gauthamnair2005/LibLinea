# AIML Utilities for Linea

# Using PyTorch (CPU and GPU) for AI/ML tasks

import torch
import torch.nn as nn
from liblinea import Linea
import numpy as np

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
    
class Inference:
    @staticmethod
    def runInference(model, input_tensor):
        if not isinstance(model, nn.Module):
            Linea.display("Provided model is not a valid PyTorch model")
            return None
        
        model.eval()  # Set the model to evaluation mode
        with torch.no_grad():  # Disable gradient calculation
            output = model(input_tensor)
        
        Linea.display(f"Inference output:\n{output}")
        return output
    
    @staticmethod
    def loadModel(model_path):
        try:
            model = torch.load(model_path)
            model.eval()  # Set the model to evaluation mode
            Linea.display(f"Model loaded from {model_path}")
            return model
        except Exception as e:
            Linea.display(f"Error loading model: {e}")
            return None
        
    @staticmethod
    def saveModel(model, model_path):
        if not isinstance(model, nn.Module):
            Linea.display("Provided model is not a valid PyTorch model")
            return False
        
        try:
            torch.save(model, model_path)
            Linea.display(f"Model saved to {model_path}")
            return True
        except Exception as e:
            Linea.display(f"Error saving model: {e}")
            return False
        
class Training:
    @staticmethod
    def trainModel(model, train_loader, criterion, optimizer, num_epochs=1):
        if not isinstance(model, nn.Module):
            Linea.display("Provided model is not a valid PyTorch model")
            return False
        
        model.train()  # Set the model to training mode
        
        for epoch in range(num_epochs):
            for inputs, targets in train_loader:
                optimizer.zero_grad()  # Zero the gradients
                outputs = model(inputs)  # Forward pass
                loss = criterion(outputs, targets)  # Compute loss
                loss.backward()  # Backward pass
                optimizer.step()  # Update weights
            
            Linea.display(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")
        
        Linea.display("Training complete")
        return True
    
class Utils:
    @staticmethod
    def tensorToNumpy(tensor):
        if not isinstance(tensor, torch.Tensor):
            Linea.display("Provided input is not a valid PyTorch tensor")
            return None
        
        numpy_array = tensor.cpu().numpy()  # Move tensor to CPU and convert to NumPy array
        Linea.display(f"Converted tensor to NumPy array:\n{numpy_array}")
        return numpy_array
    
    @staticmethod
    def numpyToTensor(numpy_array):
        if not isinstance(numpy_array, (list, tuple, np.ndarray)):
            Linea.display("Provided input is not a valid NumPy array or compatible type")
            return None
        
        tensor = torch.tensor(numpy_array)  # Convert NumPy array to PyTorch tensor
        Linea.display(f"Converted NumPy array to tensor:\n{tensor}")
        return tensor