import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
import eli5
from eli5.sklearn import PermutationImportance
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
# https://machinelearningmastery.com/multi-class-classification-tutorial-keras-deep-learning-library/
# https://machinelearningmastery.com/save-load-keras-deep-learning-models/

# load dataset
dataframe = pandas.read_csv("mbti-dataset.txt", header=None)
dataset = dataframe.values
X = dataset[:,0:60].astype(float)
Y = dataset[:,60]

# print(Y)
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)
print(dummy_y)

def create_model():
    model = Sequential()
    model.add(Dense(50, input_dim=60, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(16, activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # model.fit(X, dummy_y, epochs=200)
    return model

# model = create_model()
# model.fit(X, dummy_y, epochs=200)

# _, accuracy = model.evaluate(X, dummy_y)
# print('Accuracy: %.2f' % (accuracy*100))

estimator = KerasClassifier(build_fn=create_model, epochs=200)
estimator.fit(X, dummy_y)

perm = PermutationImportance(estimator, random_state=1).fit(X, dummy_y)
eli5.show_weights(perm)
