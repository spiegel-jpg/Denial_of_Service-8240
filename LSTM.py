# from tutorial at: https://pythonalgos.com/long-short-term-memory-lstm-in-keras/

# Import needed libraries

import tensorflow as tf 
from tensorflow import keras 
from tensorflow.keras import layers 

""" All that's really required for an LSTM neural network is that is has to have
    LSTM cells or at least one LSTM layer. If we add different types of layers
    and cells, we can still call our neural network an LSTM, but it would be more
    accurate to give it a mixed name.
    
    To build an LSTM, the first thing we need to do is initialize a Sequential model.
    Afterwards, we'll add an LSTM layer. This is what makes this an LSTM neural network.
    Then we'll add a batch normalization layer and a dense output layer. Next, we'll
    print it out to get an idea of what it looks like. """

model = keras.Sequential()
model.add(layers.LSTM(64, input_shape=(None, 28)))
model.add(layers.BatchNormalization())
model.add(layers.Dense(10))
print(model.summary())

""" You'll see from the above print that an LSTM has many, many parameters. In fact,
    it has around 4 times as many params as a simple RNN, but this is due to the fact
    that an LSTM layer has 4 gates that are critical to its operation. """

""" The MNIST dataset is a classic dataset to train and test neural networks on. It is
    a set of handwritten digits. Let's see how our built LSTM does on this dataset.

    The first thing we need to do is load up the MNIST dataset from Keras. We'll use
    the load_data() function from the MNIST dataset to load a pre-separated training
    and testing dataset. After loading the datasets, we'll normalize the training data by dividing
    by 255. This is due to the scale of 256 (0 to 255) for the image data. Finally,
    we'll set aside 10 test data points. """

mnist = keras.datasets.mnist 
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0
x_validate, y_validate = x_test[:-10], y_test[:-10]
x_test, y_test = x_test[-10:], y_test[-10:]

""" Now that we've created our LSTM and loaded up our data, let's compile our model. We have to compile
    or build the model before we can train/test it. In our model compilation we will specify
    the loss function, in this case Sparse Categorical Cross Entropy, our optimizer,
    stochastic gradient descent, and our metric, accuracy. We can specify multiple metrics,
    but we'll just go with accuracy for this example. """

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer="sgd",
    metrics=["accuracy"],
)

""" Now that the model is compiled, let's train it. To train the model in Keras, we just
    call the fit function. To use the fit function, we'll need to pass in the training
    data for x and y, the validation, the batch_size, and the epochs. For this example,
    we'll just train for 10 epochs. """

model.fit(
    x_train, y_train, validation_data=(x_test, y_test), batch_size=64, epochs=1
)
model.fit(
    x_train, y_train, validation_data=(x_validate, y_validate), batch_size=64, epochs=10
)

""" The last thing to do is to test the model. We'll run our model and use it to predict the
    sample we set aside earlier. Then, we'll print out the sample and the correct label. """

for i in range(10):
    result = tf.argmax(model.predict(tf.expand_dims(x_test[i], 0)), axis=1)
    print(result.numpy(), y_test[i])

""" You should see an accuracy of ~96% when testing for 10 epochs """