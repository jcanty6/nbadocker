#!/usr/bin/env python

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

p1 = pd.read_csv('stats2015.csv')
p2 = pd.read_csv('stats2016.csv')
p3 = pd.read_csv('stats2017.csv')
p4 = pd.read_csv('stats2018.csv')
p5 = pd.read_csv('stats2019.csv')
p6 = pd.read_csv('stats2020.csv')

train = pd.concat([p1,p2,p3,p4,p5],axis=0,sort=False)
train = train.dropna()
train = train.drop(['MP','Tm','Pos','Player'],axis=1)

test = p6.dropna()
test = test.drop(['MP','Tm','Pos','Player'],axis=1)
test2 = p6.dropna()

X = train.drop(columns='All_Star') 
y = train[['All_Star']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
randomforest = RandomForestClassifier(random_state=0, n_jobs=-1)
randomforest = randomforest.fit(X_train,y_train)

y_pred = randomforest.predict(X_test)

y_pred_test = randomforest.predict(test)

answers = test2[['Player']]

answers['as_test'] = y_pred_test

print(answers)