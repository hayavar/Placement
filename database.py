import sqlite3
from pandas import *
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib
import collections, numpy
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn import tree
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score




uname=input("Enter the name")
usn=input("Enter usn")
db=sqlite3.connect("std")
cnn=db.cursor()
sql="SELECT * FROM Student WHERE USN=? AND NAME=?"
cnn.execute(sql,[usn,uname])
row=cnn.fetchone()
global sie
global apt
global gd
global pi
if row:
    print("Student found\n")
    cer = "SELECT * FROM marks WHERE USN=?"
    cnn.execute(cer,[usn])
    row1=cnn.fetchone()
    if row1:
        print("Name: ",uname)
        name=uname
        print("USN: ",row1[0])
        USN=row1[0]
        print("SIE: ",row1[1])
        sie=row1[1]
        print("APT: ",row1[2])
        apt=row1[2]
        print("GD: ",row1[3])
        gd=row1[3]
        print("PI: ",row1[4])
        pi=row1[4]
    else:
        print("NO records found\n")
else:
    print("No records found")
    exit(0)
cnn.close()


data=pd.read_csv("placement_data.csv",sep=",")

y=data.target
x=data.drop('target',axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.7,random_state=2)

model = tree.DecisionTreeClassifier(max_depth=5,max_leaf_nodes=10,criterion='entropy')
model.fit(x_train, y_train)
y_predict = model.predict([[sie,apt,gd,pi]])
print(y_predict)


