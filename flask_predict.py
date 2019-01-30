### Try with IRIS dataset

## Using Sepal length, sepal width, petal length, petal width as inputs, predict type of flower

## Build a xgboost classifier which will classify the iris flower

import xgboost as xgb

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score

import pickle

import pandas as pd 

import numpy as np
### load the data

iris = load_iris()

# input vector
X = iris.data

Y = iris.target

## Split into train and test
print(iris)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 13,test_size = 0.3)

## Build the XGB model

dtrain = xgb.DMatrix(X_train, label=Y_train)

dtest = xgb.DMatrix(X_test, label=Y_test)

param = {
    'max_depth': 4,  # the maximum depth of each tree
    'eta': 0.1,  # the training step for each iteration
    'objective': 'multi:softprob',  # error evaluation for multiclass training
    'num_class': 3}  # the number of classes that exist in this datset
num_round = 20  # the number of training iterations

#Train the model
clf= xgb.train(param, dtrain, num_round)

# Predict on the test set
preds = clf.predict(dtest)

#Take the max of the 3 
best_preds = np.asarray([np.argmax(line) for line in preds])

### Pickle the model - a model can be saved as a binary file

print(best_preds)

with(open('./xgb.pkl','wb')) as model_pkl:
	pickle.dump(clf,model_pkl)


