'''
file to import all the necessary files
Dataset from Kaggle : Instagram Fake Profile Prediction'''


import os 
import pandas as pd


def load_train_data():
    cwd = os.getcwd()
    train_data = pd.read_csv(cwd + '/dataset/train.csv')
    return train_data

def load_test_data():
    cwd = os.getcwd()
    test_data = pd.read_csv(cwd + '/dataset/test.csv')
    return test_data



