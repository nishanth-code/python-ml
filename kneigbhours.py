from sklearn import datasets
from sklearn import metrics as sm
iris = datasets.load_iris()
data=iris.data
target = iris.target 

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(data,target,test_size=0.3)


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(xtrain,ytrain)
y_pred = classifier.predict(xtest)

target_name=iris.target_names

for pred,actual in zip(y_pred,ytest):
    print(target_name[pred],target_name[actual])


print(sm.confusion_matrix(ytest,y_pred))
print(sm.classification_report(ytest,y_pred))
