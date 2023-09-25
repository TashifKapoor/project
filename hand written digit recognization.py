# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qmRcP8JKAxF2TL_SaxsESKdLZt98n9nw
"""

from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

mnist = fetch_openml('mnist_784')

x, y = mnist['data'], mnist['target']

some_digit = x.to_numpy()[36001]
some_digit_image = some_digit.reshape(28, 28)

plt.imshow(some_digit_image, cmap=matplotlib.cm.binary,
           interpolation='nearest')
plt.axis("off")
plt.show()

x_train, x_test = x[:60000], x[6000:70000]
y_train, y_test = y[:60000], y[6000:70000]

from sklearn.utils import shuffle

shuffle_index = np.random.permutation(60000)
x_train, y_train = shuffle(x_train, y_train, random_state=42)

y_train = y_train.astype(np.int8)
y_test = y_test.astype(np.int8)
y_train_2 = (y_train == 2)
y_test_2 = (y_test == 2)

clf = LogisticRegression()
clf.fit(x_train, y_train_2)
example = clf.predict([some_digit])
print(example)

a = cross_val_score(clf, x_train, y_train_2, cv=3, scoring="accuracy")

print(a.mean())

