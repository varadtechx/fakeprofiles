
# Instagram Fake Profile Detector

## Problem Statement

The goal of this project is to develop a machine learning model that can accurately detect fake profiles on Instagram. Fake profiles on social media platforms like Instagram can be created for various malicious purposes, such as spreading spam, conducting phishing attacks, or engaging in online scams. Identifying and removing these fake profiles is crucial to maintaining a safe and reliable online environment for users.

## Dataset

The dataset used for this project consists of a collection of Instagram profiles labeled as either genuine or fake. Each profile is represented as a set of features that describe various aspects of the profile, such as follower count, post frequency, engagement rate, and more. The dataset has been curated to ensure the privacy and security of real users.

## Project Structure

The project is organized into several modules, each serving a specific purpose:

1. `train.py`: This script is responsible for training the machine learning model. It loads the dataset, preprocesses the data, builds the model architecture defined in `model.py`, compiles the model, and then trains it using the training data.

2. `model.py`: This module contains the definition of the Instagram Fake Profile Detection model. It uses TensorFlow and Keras to create the architecture of the neural network model.

3. `dataset.py`: The `dataset.py` module provides functions to load and preprocess the dataset. It handles data loading, splitting the data into training and testing sets, and applying necessary data transformations.

4. `utils.py`: This module contains utility functions that are used across different parts of the project. It may include functions for data preprocessing, evaluation metrics, or any other utility functions required during training and testing.

5. `requirements.txt`: The `requirements.txt` file lists all the required Python libraries and their versions. It ensures that anyone running the code can install the necessary dependencies easily using `pip`.

## Getting Started

To run the project, follow these steps:

1. Clone the repository to your local machine.

2. Create a new Conda environment and activate it:

```bash
   conda create -n insta_fake_detector python=3.11.4
   conda activate insta_fake_detector
```


3. Install the required packages:

```bash  
   pip install -r requirements.txt
```

4. Run train.py to start the training.


This will start the training process and save the trained model in the `weights` directory.

## Model Architecture

The Instagram Fake Profile Detection model architecture is defined in the `model.py` file using TensorFlow and Keras. The model is designed as a deep neural network with several layers of dense units. The architecture is chosen to capture complex patterns in the profile data and learn to differentiate between genuine and fake profiles effectively.

## Model Evaluation

Once the model is trained, it can be evaluated using the test dataset to assess its performance. The evaluation metrics, such as accuracy, precision, recall, and F1-score, will be used to measure the model's effectiveness in detecting fake profiles.

## Conclusion

The Instagram Fake Profile Detector is a valuable tool to identify and combat the presence of fake profiles on social media platforms. By building and training a machine learning model on a curated dataset, we can achieve a robust and accurate fake profile detection system, contributing to a safer online environment for users.

Feel free to contribute to the project by experimenting with different model architectures, data preprocessing techniques, or evaluation metrics to improve the model's performance. Let's work together to make social media platforms more secure and reliable for everyone!

>>>>>>> bec2c22 (version_1)
