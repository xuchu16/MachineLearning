#usr/bin/python
# -*- coding:utf-8 -*-

# File Name:    preprocessing.py
# Function:     this scripts used for learn sklearn.preprocessing , I just put several functions widely used 
# Created by:   xuc@shbio.com, xuchu16@163.com
# Created on:   2018/3/11 (ver 1.00.01)
# Revised hist: revised by _____ on ____/__/__ (ver 1.xx.01)(change:__)

import numpy as np
from sklearn import preprocessing

#ndarray data
data = np.array([[3, -1.5, 2, -5.4],[0, 4, -0.3, 2.1], [1, 3.3, -1.9, -4.3]])


# Mean removal
data_Mean_removal = preprocessing.scale(data)

#data Scaling
data_scaler = preprocessing.MinMaxScaler(feature_range = (0,3))#将特征值缩放到0-3
data_scaled = data_scaler.fit_transform(data)

#Normalization
data_normalized = preprocessing.normalize(data, norm= 'l1')# L1范数即特征向量的数值之和为1

#Binarization
data_binarized = preprocessing.Binarizer(threshold=1.4).transform(data)

#独热编码暂时没看懂
print('ndarray',data)
print('removal',data_Mean_removal)
print('Scaling',data_scaled)
print('normalized',data_normalized)
print('binarized',data_binarized)


