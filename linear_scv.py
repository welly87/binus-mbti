
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.feature_selection import SelectKBest, f_classif

print("Import some data to play with")

dataframe = pd.read_csv("mbti-dataset2867.txt", header=None)
dataset = dataframe.values
X = dataset[:,0:60].astype(float)
y = dataset[:,60]

print("split dataset")

X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, random_state=0
)

print("Start train linear svc without features selection")
clf = make_pipeline(LinearSVC())
clf.fit(X_train, y_train)

print('Classification accuracy without selecting features: {:.3f}'.format(clf.score(X_test, y_test)))

print("Start train linear svc with features selection")
clf_selected = make_pipeline(SelectKBest(f_classif, k=20), LinearSVC())
clf_selected.fit(X_train, y_train)

print('Classification accuracy after univariate feature selection: {:.3f}'.format(clf_selected.score(X_test, y_test)))
