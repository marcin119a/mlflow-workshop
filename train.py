import mlflow
import matplotlib.pyplot as plt
from utilities import create_dataset
	
import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from sklearn.metrics import mean_squared_error
import sys


if __name__ == "__main__": 
    file_name = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    
