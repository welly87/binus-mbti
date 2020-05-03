import pandas
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from tensorflow.keras import utils

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
dummy_y = utils.to_categorical(encoded_Y)
print(dummy_y)

def create_model():
    model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(50, input_dim=60, activation='relu'),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(16, activation='softmax')
    ])

    model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# model = create_model()
# model.fit(X, dummy_y, epochs=200)

# _, accuracy = model.evaluate(X, dummy_y)
# print('Accuracy: %.2f' % (accuracy*100))



# from keras.wrappers.scikit_learn import KerasClassifier
import eli5
from eli5.sklearn import PermutationImportance

estimator = tf.keras.wrappers.scikit_learn.KerasClassifier(build_fn=create_model, epochs=150, verbose=0)

perm = PermutationImportance(estimator, random_state=1).fit(X, dummy_y)
eli5.show_weights(perm)
