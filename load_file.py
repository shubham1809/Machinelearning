# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:28:59 2017

@author: shubham
"""
import numpy
from pandas import read_csv

#==============================================================================
# #read the input file 
#encoding is used because input may have anytype data
#
#header_names =header name of any csv file .csv file does not contain header
#==============================================================================
header_names=['Short Desc','EPH','	BBBY Primary Navigation Category Desc']
data=read_csv(r'F:\SHUBHAM\MachineLearning\POC\Data\input.csv',names=header_names,header=None,encoding='"ISO-8859-1"',dtype=str)
dataset=data.values

#inputdata having first two rows
#output having last rows
Input_data=dataset[:,0:1]
a=Input_data.tolist

#Input_data=dataset[:,0]
Output_data=dataset[:,2]
