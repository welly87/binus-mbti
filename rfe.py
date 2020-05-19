# import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification
import pandas as pd

dataframe = pd.read_csv("mbti-dataset2867.txt", header=None)
dataset = dataframe.values
X = dataset[:,0:60].astype(float)
y = dataset[:,60]

print("# Create the RFE object and compute a cross-validated score.")

svc = SVC(kernel="linear")

print("# The accuracy scoring is proportional to the number of correct")
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
              scoring='accuracy')

print(rfecv.fit(X, y))

print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
# plt.figure()
# plt.xlabel("Number of features selected")
# plt.ylabel("Cross validation score (nb of correct classifications)")
# plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
# plt.show()