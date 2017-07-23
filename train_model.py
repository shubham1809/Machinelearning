# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:30:45 2017

@author: shubham
"""

from sklearn.neighbors import KNeighborsClassifier
import split_data
import sklearn
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_iris

# Spot Check Algorithms
#==============================================================================
# it is all supervised alf=gorithim.from which we can decide 
#which algorithim we need to choose.
#==============================================================================
#models = []
#models.append(('LR', LogisticRegression()))
#models.append(('LDA', LinearDiscriminantAnalysis()))
#models.append(('KNN', KNeighborsClassifier()))
#models.append(('CART', DecisionTreeClassifier()))
#models.append(('NB', GaussianNB()))
#models.append(('SVM', SVC()))
## evaluate each model in turn
#results = []
#names = []
#for name, model in models:
#	kfold = sklearn.model_selection.KFold(n_splits=10, random_state=7)
#	cv_results = sklearn.model_selection.cross_val_score(model, split_data.X_train,split_data.y_train, cv=kfold, scoring='accuracy')
#	results.append(cv_results)
#	names.append(name)
#	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
#	print(msg)


dtc=DecisionTreeClassifier()

dtc.fit(split_data.X_train,split_data.y_train)

y_pred=dtc.predict(split_data.X_test)
print("Cart model acuracy: ",metrics.accuracy_score(split_data.y_test,y_pred))

knn=KNeighborsClassifier()
knn.fit(split_data.X_train,split_data.y_train)

y_pred=knn.predict(split_data.X_test)

print("KNN model acuracy: ",metrics.accuracy_score(split_data.y_test,y_pred))

print(split_data.X_train.shape())
#

#import encoding
#x=encoding.decoded_output(0)
#print(x)
#import pandas as pd
#header_names=['Short Desc','EPH']
#data=pd.read_csv(r'F:\SHUBHAM\MachineLearning\POC\Data\input.csv',names=header_names,header=None,encoding='"ISO-8859-1"',dtype=str)
#dataset=data.values
#
##inputdata having first two rows
##output having last rows
#Input_data=dataset[:,0:2]
#
#import encoding
#test_input= encoding.encoding_input(Input_data)
#y_pred=knn.predict(test_input)