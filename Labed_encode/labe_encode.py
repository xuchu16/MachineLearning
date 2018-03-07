#usr/bin/python
# -*- coding:utf-8 -*-

# File Name:    labelencode.py
# Function:     this scripts used for learn sklearn.preprocessing , I just put several functions widely used 
# Created by:   xuc@shbio.com, xuchu16@163.com
# Created on:   2018/3/11 (ver 1.00.01)
# Revised hist: revised by _____ on ____/__/__ (ver 1.xx.01)(change:__)

# 在监督学习中要处理各种各样的标记，这些标记可能是数字，也可能是单词，如果标记是数字，则算法可以直接使用,而如果是单词，则要把单词标记为数值再操作


import numpy as np
from sklearn import preprocessing

#这是一个以单词为标记的序列
input_class = ['audi','frod','audi','toyota','ford','bmw']

#先定义一个标记编码器，并利用之前的序列对该标记编码器进行训练
label_encoder = preprocessing.LabelEncoder()#这样写的话只是把单词标记转化为索引
label_encoder.fit(input_class)

#for i,item in enumerate(label_encoder.classes_):
#    print (i,item)

#之后就可以用这个标记编码器对之后遇到的单词标记转化为索引
labels = ['audi','toyota','bmw']
encode_labels = label_encoder.transform(labels)

#对数值特征反转
decoded_labels = label_encoder.inverse_transform(encode_labels)
print(encode_labels)
print(decoded_labels)



