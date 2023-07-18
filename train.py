import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import Accuracy

from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,accuracy_score,roc_curve,confusion_matrix
from sklearn.preprocessing import StandardScaler, MinMaxScaler

import os 
import pandas as pd

from dataset import load_train_data,load_test_data

from model  import seq 


train_data=load_train_data()

test_data=load_test_data()

X_train = train_data.drop(columns='fake')
X_test = test_data.drop(columns='fake')

y_train = train_data['fake']
y_test = test_data['fake']

scaler_x = StandardScaler()
X_train = scaler_x.fit_transform(X_train)
X_test = scaler_x.transform(X_test)

y_train = tf.keras.utils.to_categorical(y_train, num_classes = 2)
y_test = tf.keras.utils.to_categorical(y_test, num_classes = 2)

print('Training Starting ...................')

model = seq()

model.compile( optimizer = 'adam', loss = 'categorical_crossentropy , metrics = ['accuracy'] 
model.compile( optimizer = 'adam', loss = 'categorical_crossentropy , metrics = ['accuracy'])


epochs_hist = model.fit(X_train, y_train, epochs = 50,  verbose = 1, validation_split = 0.1)



predicted = model.predict(X_test)

