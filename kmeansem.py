import pandas as pd
import numpy as np
from sklearn import datasets
import sklearn.metrics as sm
import matplotlib.pyplot as plt


iris = datasets.load_iris()


x= pd.DataFrame(iris.data)
x.columns=['sepal_l','sepal_w','petal_l','petal_w']

y = pd.DataFrame(iris.target)
y.columns=['target']

plt.figure(figsize=(14,7))
colormap = np.array(['red','lime','black'])

plt.subplot(1,3,1)
plt.scatter(x.petal_l,x.petal_w,c=colormap[y.target],s=40)
plt.title('real class')
plt.xlabel('petal_l')
plt.ylabel('petal_w')

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(x)
plt.subplot(1,3,2)
plt.scatter(x.petal_l,x.petal_w,c=colormap[model.labels_],s=40)
plt.title('k means')
plt.xlabel('petal_l')
plt.ylabel('petal_w')


from sklearn.mixture import GaussianMixture
gnm = GaussianMixture(n_components=3)
gnm.fit(x)
y_g = gnm.predict(x)

plt.subplot(1,3,3)
plt.scatter(x.petal_l,x.petal_w,c=colormap[y_g],s=40)
plt.title('em ')
plt.xlabel('petal_l')
plt.ylabel('petal_w')
