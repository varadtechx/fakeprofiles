import os 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from dataset import load_train_data , load_test_data





def dataset_info():
    train_data = load_train_data()
    print(train_data.shape)
    print(train_data.columns)
    print(train_data.dtypes)
    print(train_data.head())
    print(train_data.info())


def test_dataset_info():
    test_data = load_test_data()
    print(test_data.shape)
    print(test_data.columns)
    print(test_data.dtypes)
    print(test_data.head())
    print(test_data.info())


def corelation_dataset():
    train_data = load_train_data()
    # test_data = load_test_data()
    plt.figure(figsize=(20, 20))
    cm = train_data.corr()
    ax = plt.subplot()
    sns.heatmap(cm, annot = True, ax = ax)
    plt.show()



def classsification_results():
    # predicted_value = []
    # test = []
    # for i in predicted:
    #     predicted_value.append(np.argmax(i))
    
    # for i in y_test:
    #     test.append(np.argmax(i))

    # print(classification_report(test, predicted_value))

    # plt.figure(figsize=(10, 10))
    # cm=confusion_matrix(test, predicted_value)
    # sns.heatmap(cm, annot=True)
    # plt.show()
    
    return None