from sklearn import datasets
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
iris = datasets.load_iris()
digits = datasets.load_digits()

print(iris)

data = pd.DataFrame(iris.data)
data.columns=['Sepal length','Sepal width','Petal length','Petal width']
feature = data[['Sepal length','Sepal width']]

# create model and prediction
model = KMeans(n_clusters=4, algorithm='auto')
model.fit(feature)
predict = pd.DataFrame(model.predict(feature))
predict.columns=['predict']

# concatenate labels to df as a new column
r = pd.concat([feature,predict], axis=1)
# print(r)

# centers = pd.DataFrame(model.cluster_centers_, columns=['Sepal length','Sepal width'])
# center_x = centers['Sepal length']
# center_y = centers['Sepal width']

# # scatter plot
# plt.scatter(r['Sepal length'], r['Sepal width'], c=r['predict'], alpha=0.5)
# plt.scatter(center_x, center_y , s=50, marker='D', c='r')
# plt.show()