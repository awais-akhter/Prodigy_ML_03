# -*- coding: utf-8 -*-
"""image-classification-dog-and-cat.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HE2n-uTf46b7ELbk4SlB4-YK-Nxi4rn5

# **Prodigy Infotech - Machine Learning Internship**

# **TASK 1 - Image Classification using SVM**

### Author : Muhammad Awais Akhter

[![alt text](https://logoeps.com/wp-content/uploads/2014/02/25231-github-cat-in-a-circle-icon-vector-icon-vector-eps.png "Git Hub Link")](https://github.com/awais-akhter)

### Problem Statement: Implement a support vector machine (SVM) to classify images of cats and dogs from the Kaggle dataset.

### Dataset link :- https://www.kaggle.com/c/dogs-vs-cats/data

### Importing the neccesary Libraries
"""

import numpy as np
import pandas as pd
import zipfile
import os
from PIL import Image
from sklearn.model_selection import train_test_split
from skimage.feature import hog
from skimage import data, exposure
from skimage.transform import rescale, resize

import warnings
warnings.filterwarnings("ignore")

"""### Loading the dataset and getting info about it"""

data_set = "dogs-vs-cats"

with zipfile.ZipFile("/kaggle/input/"+ data_set +"/train.zip","r") as z:
    z.extractall(".")

    destination = '/kaggle/files/images'
    z.extractall(destination)

data_ = pd.DataFrame({'file': os.listdir('/kaggle/files/images/train')})
print(data_.head())

Y=[]
for i in os.listdir('/kaggle/files/images/train'):
    if 'dog' in i:
        Y.append(1)
    else:
        Y.append(0)


data_['class'] = Y
print(data_.head())

file = data_['file']

Y = data_['class']

"""### Visualizing Data"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import random

plt.figure(figsize=(16,16))

images = os.listdir('/kaggle/files/images/train')
for i in range(8):
    img = random.choice([x for x in images])
    fig = plt.subplot(4,4,i+1)
    fig.axis('off')
    img = mpimg.imread(os.path.join('/kaggle/files/images/train', img))
    fig.imshow(img)

data_size = 1200
ptr=0
X = []
for i in file:
    img = mpimg.imread('/kaggle/files/images/train/' + i)
    resized_img = resize(img , (128 , 64))
    fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),cells_per_block=(2, 2), visualize=True, channel_axis=-1)
    X.append(fd)
    ptr = ptr+1
    if(ptr >= data_size):
        break

"""### Separating features and Spiting Data"""

Y = Y[:data_size]

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

"""### SVC Linear Model"""

from sklearn.svm import LinearSVC
c=1
svm_LinearSVC = LinearSVC(C=c).fit(X_train, y_train)
accuracy = svm_LinearSVC.score(X_test, y_test)
print('SVC Linear Accuracy: ' + str(accuracy))

"""### SVC-SVM Model accuracy"""

from sklearn.svm import SVC
svm_svc = SVC(kernel='linear', C=c).fit(X_train, y_train)
accuracy = svm_svc.score(X_test, y_test)
print('Svm-Svc Accuracy: ' + str(accuracy))

"""### Conclusion - As we can see the model is giving accuracy of 0.68 approx."""