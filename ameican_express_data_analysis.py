# -*- coding: utf-8 -*-
"""Ameican_Express_Data_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KxznPq1NSA0rv1QXr6uAT9Qwp-ztPv9k

# Deep Learning via ANN

## Importing libraries
"""

import numpy as np
import pandas as pd
import tensorflow as tf

tf.__version__

"""## Importing dataset"""

dataset = pd.read_csv('American.csv')
X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

print(X)

"""## Encoding categorical data

### Gender column : Label Encoding
"""

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
X[:, 2] = label_encoder.fit_transform(X[:, 2])

print(X)

"""### Geography column : One hot Encoding"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""## Splitting dataset into Training & Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""## ANN

### Initialization
"""

ann = tf.keras.models.Sequential()

"""### Adding input layer and first hidden layer"""

ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

"""### Adding second hidden layer"""

ann.add(tf.keras.layers.Dense(units=6, activation='relu'))

"""### Adding output layer"""

ann.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

"""## ANN Training

### Compiling ANN
"""

ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

"""### Training on training dataset"""

ann.fit(X_train, y_train, batch_size = 32, epochs = 120)

"""# Predictions

### Single Prediction
"""

print(ann.predict(sc.transform([[0.0, 1.0, 0.0, 501, 0, 32, 2, 0.0, 4, 1, 545501]])) > 0.5)

"""### Predication on testset"""

y_pred = ann.predict(X_test)
y_pred = (y_pred > 0.5)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""### Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)