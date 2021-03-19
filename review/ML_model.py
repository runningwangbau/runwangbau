import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from string import ascii_lowercase
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.ensemble import ExtraTreesClassifier



def Analy_model():
    train=pd.read_csv("train.csv")
    eda_train=train.copy()

    encoder=LabelEncoder()
    eda_train['age_group']=encoder.fit_transform(eda_train['age_group'])
    eda_train['religion']=encoder.fit_transform(eda_train['religion'])
    eda_train['race']=encoder.fit_transform(eda_train['race'])
    eda_train['gender']=encoder.fit_transform(eda_train['gender'])

    num=[i for i in list(ascii_lowercase)[:20]]

    eda_train.drop(eda_train[[('Q'+i+'E')for i in num]],axis=1,inplace=True)
    eda_train.drop('index',axis=1,inplace=True)

    del eda_train['wf_01']
    del eda_train['wf_02']
    del eda_train['wf_03']
    del eda_train['wr_01']
    del eda_train['wr_02']
    del eda_train['wr_03']
    del eda_train['wr_04']
    del eda_train['wr_05']
    del eda_train['wr_06']
    del eda_train['wr_07']
    del eda_train['wr_08']
    del eda_train['wr_09']
    del eda_train['wr_10']
    del eda_train['wr_11']
    del eda_train['wr_12']
    del eda_train['wr_13']


    y=eda_train['voted']
    eda_train.drop('voted',axis=1,inplace=True)
    y=pd.get_dummies(y)
    X=eda_train.values
    Y=y.values

    min_max_scaler=preprocessing.MinMaxScaler()
    X_scale=min_max_scaler.fit_transform(X)
    X_train,X_test,y_train,y_test=train_test_split(X_scale,Y,test_size=0.3,random_state=123)
    xtree=ExtraTreesClassifier(bootstrap=False, max_features=0.7000000000000001,criterion='gini', min_samples_leaf=14, min_samples_split=7, n_estimators=100)
    analy_model=xtree.fit(X_train, y_train)

    return analy_model







