###########################
#Program written by Brendan DeMilt
###########################
import numpy, math
import tensorflow as tf
from tensorflow import keras

###############
#Creating Dataset
###############
reader = open("Training_Data.txt", "r")

words = []
syllables = []

#splits words and count into the same index of two separate arrays
#then putting them together in a tf dataset
for line in reader:
    text = line.split("-")
    temp = list(text[0])
    for i in range(len(temp)):
        temp[i] = ord(temp[i])
    words.append(temp)
    syllables.append((int(text[1][0])))

# in/output maximums computed from TrainingDataFormatter.py
word_max = 143
sylMax = 7


#Creating a model with one hidden layer with 30 nodes
model = keras.Sequential()
model.add(keras.layers.Embedding(word_max, 100))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(100, activation = tf.nn.relu))
model.add(keras.layers.Dense(50, activation = tf.nn.relu))
model.add(keras.layers.Dense(8, activation = tf.nn.softmax))
model.summary()


#might consider switching to GradientDescent but will keep for now
model.compile(optimizer=tf.train.GradientDescentOptimizer(learning_rate = 0.2,
                                                          use_locking = False),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

#separating training from testing data

test_in = numpy.array(words[:10000])
train_in = numpy.array(words[10000:])

test_out = numpy.array(syllables[:10000])
train_out = numpy.array(syllables[10000:])


history = model.fit(train_in, train_out, epochs=80, batch_size=500,
                    validation_data=(test_in, test_out),
                    verbose=2)

results = model.evaluate(test_in[:100], test_out[:100])
print("Test Accuracy: ", results[1])

