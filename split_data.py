# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:30:31 2017

@author: shubham
"""

from sklearn.model_selection import train_test_split

import encoding
import load_file

X_train,X_test,y_train,y_test=train_test_split(encoding.encoding_input(load_file.Input_data),encoding.encoded_output(load_file.Output_data),test_size=0.2,random_state=1)
#X_train,X_test,y_train,y_test=train_test_split(encoding.encoded_output1(load_file.Input_data),load_file.Output_data,test_size=0.2,random_state=1)