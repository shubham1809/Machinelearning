# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:31:02 2017

@author: shubham
"""
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
le=LabelEncoder()
a=['shubham','dpdnw']
#le.fit(a)
#print(le.classes_)
a1=le.fit_transform(a)
oe=OneHotEncoder()
print(a1.reshape(a.shape[0],1))
print(le.inverse_transform(0))