#usr/bin/python
# -*- coding:utf-8 -*-

# File Name:    Linear_Regression.py
# Function:     this scripts used for learn sklearn.preprocessing , I just put several functions widely used 
# Created by:   xuc@shbio.com, xuchu16@163.com
# Created on:   2018/3/11 (ver 1.00.01)
# Revised hist: revised by _____ on ____/__/__ (ver 1.xx.01)(change:__)

# 逻辑回归用于分类

import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#这是一个以单词为标记的序列
COADREAD = pd.read_table('genomicMatrix_COADREAD',index_col = 0)
print(COADREAD)
data = np.array(COADREAD)
#print(data)
y = []
for i in range(20530):
    y.append(i+1)
Y = np.array(y)
y_pred = KMeans(n_clusters=2, random_state=100).fit_predict(data)






