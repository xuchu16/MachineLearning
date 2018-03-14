#usr/bin/python
# -*- coding:utf-8 -*-

# File Name:    PCA.py
# Function:     this scripts used for learn sklearn, I just put several functions widely used 
# Created by:   xuc@shbio.com, xuchu16@163.com
# Created on:   2018/3/15 (ver 1.00.01)
# Revised hist: revised by _____ on ____/__/__ (ver 1.xx.01)(change:__)

#这个里面包含了多个降纬的方法 
#PCA 用于降维，一个向量可以由多个向量合并而成,降维只能

import pandas as pd
import numpy as np

#这是一个以单词为标记的序列

data = 'genomicMatrix_COADREAD'

def PCA(inpot_data):
    from sklearn import decomposition
    COADREAD = pd.read_table(data,index_col = 0)
    COADREAD = COADREAD.T
    #行列互换
  #  print (COADREAD.describe())
    pca = decomposition.PCA()#创建一个PCA对象 
    pca.fit(COADREAD)#对输入数据进行PCA分析
    variances = pca.explained_variance_#这个是打印每个纬度的方差
    thresh_variance = 2#设定一个cutoff 的方差
    num_useful_dims = len(np.where(variances > thresh_variance)[0])#用到了前面的方差,只取出一列作为长度的提取，根据方差得到我们所想要的纬度
    pca.n_components = num_useful_dims  #n_components是低纬空间大小 维度绝对不会大于原本小的那个维度可以根据方差来确定维度大小，也可以自己设定降维度后的维度大小
    COADREAD_new = pca.fit_transform(COADREAD)#执行降维的操作
    return (COADREAD,COADREAD_new,num_useful_dims) 
#    print (COADREAD_new)

if __name__ == '__main__' :
    (data_original,data_pca,dim) =  PCA(inpot_data = data)
    print (data_original,data_pca,dim)
    




