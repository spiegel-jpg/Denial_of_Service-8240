

# Import needed libraries

import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers 
from numpy import array
from keras.models import Sequential
from keras.layers import LSTM

# define model where LSTM is also output layer

""" To stack LSTM layers, we need to let the configuration of the prior LSTM layer output
    a 3D array as input for the subsequent layer. We can do this by setting the return_sequences
    argument on the layer to True. This will return one output for each input time step
    and provide a 3D array."""

""" A dropout on the input means that for a given probability, the data on the input connection to 
    each LSTM block will be excluded from node activation and weight updates. In Keras, this is specified
    with a dropout argument when creating an LSTM layer. The droput value is a percentage between
    0 (no dropout) and 1 (no connection).
    
"""

"""
    Below is the setup for a Stacked LSTM according to the specifications given in Section 5.1
    of the research paper. Here we have an input layer with 4 neurons, followed by a dropout layer
    of 10%. Next is the first hidden layer with 512 neurons with 10% dropout. Next is the second
    hidden layer with 256 neurons and 10% dropout. Finally there is the third hidden layer with
    64 neurons and 10% dropout. The model is concluded with a Dense output layer consisting of
    1 neuron and the sigmoid activation function.

    We compile the model with the Binary Cross Entropy loss function and the sgd optimizer.

    ***POINTS TO NOTE:
        1) The input_shape parameter in the input layer is 3,1 as a placeholder, as I am not sure
            what it's actual value needs to be for our purposes
        2) While the paper states that the input layer and each hidden layer has dropout, it does not
            state how much dropout to use, or if all layers use the same dropout value, so 10% here
            is also a placeholder
        3) I am still trying to understand the concept of an optimizer, so I have kept the sgd optimizer
            that I used in the first LSTM.py file, but this may need to be changed as well
"""

model = Sequential()
model.add(LSTM(4, return_sequences=True, input_shape=(3,1), dropout=0.1))
model.add(LSTM(512, return_sequences=True, dropout=0.1))
model.add(LSTM(256, return_sequences=True, dropout=0.1))
model.add(LSTM(64, dropout=0.1))
model.add(Dense(1, activation="sigmoid"))
model.compile(
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer='sgd'
)