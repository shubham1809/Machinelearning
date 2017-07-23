# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:29:10 2017

@author: shubham
"""
import numpy
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

def encoding_input(input_data):
    encoded_data=None
    for i in range(0,input_data.shape[1]):
        label_encoder=LabelEncoder()
        feature=label_encoder.fit_transform(input_data[:,i])
        feature=feature.reshape(input_data.shape[0],1)
        onehotencoder=OneHotEncoder(sparse=False)
        feature=onehotencoder.fit_transform(feature)
        if encoded_data is None:
            encoded_data=feature
        else:
            encoded_data=numpy.concatenate((encoded_data,feature),axis=1)
    return encoded_data


label_encoder1=LabelEncoder()
label_encoder2=LabelEncoder()
def encoded_output(output_data):
       global label_encoder2 
       label_encoder2=label_encoder1.fit(output_data)
       encoded_ouput_data=label_encoder2.transform(output_data)
       return encoded_ouput_data

label_encoder3=LabelEncoder()
label_encoder4=LabelEncoder()
def encoded_output1(output_data):
       global label_encoder4 
       label_encoder4=label_encoder3.fit(output_data)
       encoded_ouput_data=label_encoder3.transform(output_data)
       return encoded_ouput_data   
   
def decoded_output(i):
    return label_encoder2.inverse_transform(i)