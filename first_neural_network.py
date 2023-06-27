# -*- coding: utf-8 -*-
"""First Neural Network.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HdGjioUDBi9SPvLqT3DuaFuBFMLvqN7k
"""

# print("Sai Ram")
!pwd

import torch
from torch import nn
import random # to generate rando numbers

# Defining Mystery function
def mystery_fn(a,b) -> torch.tensor:
  return torch.tensor(a+3*b) # nn is going to take in all data as tensors

# Building NN - the Model
model = nn.Sequential(nn.Linear(2,1)) # We have 2 inputs and 1 output

# Displaying model
model

# We need to train the neural network
# To train the network there are 3 parts
# 1. To check how well the criterion is doing
# 2. To check how the NN is updated in the training process, which is the optimizer
# 3. Just the training loop itself

# Checking the criterion
criterion = nn.MSELoss()

# Optimization
optimizer = torch.optim.SGD(params = model.parameters(), lr = 0.01, momentum = 0.09)

# Training Loop
for i in range(1000):

  # Inputs
  a_train = random.random()
  b_train = random.random()

  # Desired Output
  desiredOutput = mystery_fn(a = a_train, b = b_train)

  # Model Output
  output = model(torch.tensor([a_train, b_train]))

  # Compare Model output with Desired output
  # Calling criterion
  loss = criterion(output.squeeze(), desiredOutput)

  # Track the loss thorughout the training process
  if((i % 100) == 0):
    print(f"Loss : {loss.item()}")

  # Update the weights
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()

# Testing the model
# Sample Input
a_test = 1.0
b_test = -1.0
output_test = model(torch.tensor([a_test, b_test]))
desiredOutput_test = mystery_fn(a = a_test, b = b_test)

print(output_test)
print(desiredOutput_test)
