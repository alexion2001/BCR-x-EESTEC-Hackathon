#RETEA NEURONALA - CNN

#probleme - trb sa aiba acc bag ;i acc randuri
#forma = len randuri, len bag

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical
import pickle
from sklearn.preprocessing import StandardScaler, Normalizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
from PIL import Image
import nnfs
import math
from sklearn.metrics import f1_score, accuracy_score
from matplotlib import pyplot
from sklearn.feature_extraction.text import CountVectorizer
from Extractie_Date_Extras import cheltuieli as testData
from Extractie_Date_Extras import titular,venituri

#stabilire index pentru eticheta
def index_label(label):
    if label == "MANCARE":
        index = 0
    elif label == "TRANSPORT":
        index = 1
    elif label == "CASA":
        index = 2
    elif label == "DIVERSE":
        index = 3

    return index

#citire comercianti date de train
train_comerciant = []
train_labels = []
f = open("trainExtras.txt")
for trans in f.read().split('\n'):
    file = trans.split(',')
    train_comerciant.append(file[0])
    train_labels.append(index_label(file[1]))

f.close()
train_comerciant = np.array(train_comerciant)
train_labels = np.array(train_labels)


#citire comercianti date de validation
validation_comerciant = []
validation_labels = []
f = open("validationExtras.txt")
for trans in f.read().split('\n'):
    file = trans.split(',')
    validation_comerciant.append(file[0])
    validation_labels.append(index_label(file[1]))

f.close()
validation_comerciant = np.array(validation_comerciant)
validation_labels = np.array(validation_labels)

#citire comercianti date de test - datele clientului extrase
test_comerciant = []
test_labels = []
test_value = []
#citire din fisier
# f = open("testExtras.txt")
# for trans in f.read().split('\n'):
#     file = trans.split(',')
#     test_comerciant.append(file[0])
#     test_labels.append(None)
# f.close()
#citire din lista provenita din extras
print(testData)
for trans in testData:
    test_comerciant.append(trans[0])
    test_value.append(trans[1])
    test_labels.append(None)
test_comerciant = np.array(test_comerciant)
test_labels = np.array(test_labels)

#reshape data
vectorizer = CountVectorizer()

#bag-of-words
X = vectorizer.fit_transform(train_comerciant)
input_shape_train = X.shape
vocabulary_train = vectorizer.get_feature_names_out()
X_reshaped = X.toarray().reshape(X.toarray().shape[1], -1)


Y = vectorizer.transform(validation_comerciant)
input_shape_validation = Y.shape
vocabulary_validation = vectorizer.get_feature_names_out()
Y_reshaped = Y.toarray().reshape(Y.toarray().shape[1], -1)

Z = vectorizer.transform(test_comerciant)
input_shape_test = Z.shape
vocabulary_test = vectorizer.get_feature_names_out()
Z_reshaped = Z.toarray().reshape(Z.toarray().shape[1], -1)


print(X_reshaped.shape,Y_reshaped.shape,Z_reshaped.shape)

# transformare label sub forma unei liste cu 4 elemente de 0 si un element 1 care indica numarul etichetei
matrix_train_label = np.array(to_categorical(train_labels))
matrix_validation_label = np.array(to_categorical(validation_labels))

#definirea modelului
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],))) #forma datelor de train
model.add(Dense(32, activation='relu'))
model.add(Dense(4, activation='softmax'))  #4 etichete
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

#antrenarea modelului
model.fit(X.toarray(), matrix_train_label,
                      epochs = 30,
                      validation_data=(Y.toarray(), matrix_validation_label),
                      batch_size=128)
model.fit(X.toarray(), matrix_train_label,
                      epochs = 20,
                      validation_data=(Y.toarray(), matrix_validation_label),
                      batch_size=256)
model.fit(X.toarray(), matrix_train_label,
                      epochs = 10,
                      validation_data=(Y.toarray(), matrix_validation_label),
                      batch_size=512)

# predictia pentru datele de validare
pred_labels_validation = model.predict(Y.toarray())
pred_labels_validation = np.argmax(pred_labels_validation, axis=1)

print("Accuracy:", accuracy_score(validation_labels,pred_labels_validation))

# predictia etichetelor pentru test
pred_labels_test = model.predict(Z.toarray())
pred_labels_test = np.argmax(pred_labels_test, axis = 1)

# salvarea predictiei pentru datele de testare in fisier
tranzactii = []
g = open("test_labels_cnn.txt", "w")
for i in range(len(test_comerciant)):
    pred = test_comerciant[i]+"," + str(pred_labels_test[i])+"," + str(test_value[i])+"\n"
    g.write(pred)
    tranzactii.append([test_value[i],pred_labels_test[i]])
g.close()

