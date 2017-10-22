# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


df = pd.read_excel("gui/Gwent模型.xlsx")

x,y = df.drop(['序号','结果'],axis=1),df[['结果']]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3,random_state = 10)

model = LogisticRegression()
model.fit(x_train,y_train)


print(accuracy_score(y_test,model.predict(x_test)))

model.predict(df.drop(['结果'],axis=1))
data = pd.DataFrame(model.predict(df.drop(['结果'],axis=1)))
data.columns=['LR模型预测结果']
df['LR模型预测结果'] = data['LR模型预测结果'] 
df.columns=['序号','我方MMR','敌方MMR','实际结果','LR模型预测结果']

df

model.predict([4499,4501])
model.predict([4300,4500])