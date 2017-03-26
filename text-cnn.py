# -*- coding: utf-8 -*-
from __future__ import print_function
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Reshape, Flatten, Merge
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import SGD, Adadelta, Adagrad
import sys
import numpy as np
np.random.seed(1337)

if __name__ == '__main__':
    data_path = 'data/'
    nb_epoch = int(sys.argv[1])
    nb_classes = 39
    max_len = 58
    word_dim = 300
    nb_filters = 128
    batch_size = 128
    # load data from numpy
    X_train = np.load(data_path + "x-data-train.npy")
    y_train = np.load(data_path + "y-data-train.npy")
    X_test = np.load(data_path + "x-data-test.npy")
    y_test = np.load(data_path + "y-data-test.npy")

    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], word_dim, 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], word_dim, 1))
    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test = np_utils.to_categorical(y_test, nb_classes)

    # build cnn model
    model = Sequential()
    model.add(Convolution2D(nb_filters, nb_row=3, nb_col=word_dim, activation='relu',
                            input_shape=(max_len, word_dim, 1)))
    model.add(Convolution2D(64, nb_row=2, nb_col=1, activation='relu'))
    model.add(MaxPooling2D(pool_size=(4, 1)))
    model.add(Flatten())
    model.add(Dropout(0.2))
    model.add(Dense(nb_classes, activation='softmax'))
    sgd = SGD(lr=0.7, clipnorm=1.0)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    # train model
    model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch, verbose=1, validation_data=(X_test, y_test))
    score, acc = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=1)
    print('Test score:', score)
    print('Test accuracy:', acc)
