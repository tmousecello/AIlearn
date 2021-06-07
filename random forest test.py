from sklearn.datasets import load_iris
from pprint import pprint
iris = load_iris()
pprint(iris)


from matplotlib.pyplot import figure
from sklearn.tree import DecisionTreeClassifier, plot_tree

tree = DecisionTreeClassifier(max_depth=2)
tree.fit(iris.data, iris.target)

figure(figsize=(16,9),dpi=68)
plot_tree(tree, feature_names=iris.feature_names)


import random

def bootstrap(x,y):
  n = len(x)
  assert len(y) == n
  #random.seed(0) #控制隨機
  indices = random.choices(range(n),k=n) 
  indices = set(indices) #轉成集合(不重複資料)
  indices = list(indices)
  return x[indices], y[indices]

tree = DecisionTreeClassifier(max_depth=2) #tree = DecisionTreeClassifier(max_depth=2，random_state=0)可決定隨機

x, y = bootstrap(iris.data, iris.target)
tree.fit(x,y)

figure(figsize=(16, 9),dpi=68)
plot_tree(tree, feature_names=iris.feature_names)


import random

def bootstrap(x,y):
  n = len(x)
  assert len(y) == n
  #random.seed(0) #控制隨機
  indices = random.choices(range(n),k=n) 
  indices = set(indices) #轉成集合(不重複資料)
  indices = list(indices)
  return x[indices], y[indices]

tree = DecisionTreeClassifier(max_depth=2) #tree = DecisionTreeClassifier(max_depth=2，random_state=0)可決定隨機

x, y = bootstrap(iris.data, iris.target)
tree.fit(x,y)

figure(figsize=(16, 9),dpi=68)
plot_tree(tree, feature_names=iris.feature_names)


# from sklearn.ensemble import RandomForestClassifier
# forest = RandomForestClassifier(max_depth=2)
# forest.fit(iris.data, iris.target)
# print(forest.predict(iris.data))
# 直接用套件的作法
