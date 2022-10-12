# NeuralNetwork

Datasets stored in local file as github has 100MB upload limit.

Need to download mnist_train.csv and mnist_test.csv from https://www.kaggle.com/datasets/oddrationale/mnist-in-csv

Explanations of files:
  - Train.py used to train the neural network and store the different weights and biases (still in progress)
  - Main.py contains the code the functions to the neuralnet that is used by train.py (Needs changing to better suit to be used as a module, e.g a Class)
  
Known Issues:
  - Weights are being changed to NaN's, has something to do with runtime true division error on line 32 (one of previous calculations is wrong so is dividing by 0, i just can't find it :C).
  - Code in train.py is miserable, needs to be changed.
