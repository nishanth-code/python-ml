import pandas as pd

data = pd.read_csv('data6.csv',names=['message','label'])

data['labelnum'] = data.label.map({'pos':1,'neg':0})

x = data.message
y =  data.labelnum

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
xtrain_dtm = count_vect.fit_transform(xtrain)
xtest_dtm = count_vect.transform(xtest)

print(count_vect.get_feature_names_out())

from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(xtrain_dtm,ytrain)
predicted = clf.predict(xtest_dtm)

import sklearn.metrics as sm
print(sm.accuracy_score(ytest,predicted))
print(sm.precision_score(ytest,predicted))
print(sm.recall_score(ytest,predicted))
print(sm.confusion_matrix(ytest,predicted))
