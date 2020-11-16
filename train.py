import mlflow
from utilities import create_dataset
	
import math

from model import model
import sys


if __name__ == "__main__": 
    file_name = str(sys.argv[1]) 
    number_neurons = int(sys.argv[2])
    epochs = int(sys.argv[3])
    batch_size = int(sys.argv[4])
    loss = str(loss)
    optym = str(optym)


    model, trainScore, testScore =  model(file_name, number_neurons, epochs, batch_size, loss, optym)

    mlflow.log_param("file_name", file_name)
    mlflow.log_param("number_neurons", number_neurons)
    mlflow.log_metric("rmse", trainScore)
    mlflow.keras.save_model(model, "model")
