# import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras import backend as K

from keras import optimizers
from keras.utils import to_categorical

from sklearn import preprocessing
import matplotlib.pyplot as plt
import os
import cv2
from imutils import paths
import numpy as np
import random

class cnn():
    @staticmethod
    def build():
        model = Sequential()

        model.add(Conv2D(32, (5,5), input_shape = (250, 250, 3), padding = 'same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size = (2,2), strides = (2,2)))

        model.add(Conv2D(16, (5,5), padding = 'same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size = (2,2), strides = (2,2)))

        model.add(Flatten())

        model.add(Dense(256))
        model.add(Activation('relu'))

        model.add(Dropout(0.7))

        model.add(Dense(50))
        model.add(Activation('relu'))
        
        model.add(Dense(2))
        model.add(Activation('softmax'))

        return model


def imgtoarray(path):
    
    image_data = cv2.imread(path)
    image_data = image_data - np.average(image_data)/np.std(image_data)
    return image_data

model = cnn.build()
print(model.summary())


random.seed(21)
preprocessed_images = list(paths.list_images('image_preprocessed/'))
random.shuffle(preprocessed_images)

def data():
    
    data = []
    data_label = [] 
    for image in preprocessed_images:
        
        data.append(imgtoarray(image))
        label = 1 if image.split('/')[1].find("sachin")==0 else 0
        data_label.append(label)
        
    
    return np.array(data), np.array(data_label)

dataset = data()
train_dataset = dataset[0][0:70]/255, dataset[1][0:70]

from keras.utils import to_categorical
train_y = to_categorical(np.array(train_dataset[1]))

test_dataset = dataset[0][71:]/255, dataset[1][71:]
test_y = to_categorical(np.array(test_dataset[1]))

optim = optimizers.Adam(lr = 0.001, decay = 1e-6/25)
model.compile( optimizer = optim, 
             metrics = ["accuracy"],
             loss = 'binary_crossentropy')
hist = model.fit(train_dataset[0], train_y, 
                batch_size = 6, epochs =25)

model.save("model.h5")

plt.plot(np.arange(0, 25), hist.history["loss"], label = "train_loss")
plt.show()