import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout 

def seq():

    model = Sequential()
    model.add(Dense(50, input_dim=11, activation='relu'))
    model.add(Dense(150, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(150, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(25, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(2,activation='softmax'))

    print(model.summary())

    return model


def get_summary(model):
    return model.summary()
