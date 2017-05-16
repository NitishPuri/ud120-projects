#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""


import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

outputFile = "output.txt"
out = open(outputFile, "w")

def logLine(line):
    out.write(line)
    out.write("\n")
    print line

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
labels_predict = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(labels_test, labels_predict)

logLine("Accuracy : {}".format(accuracy))
logLine("Training time : {}".format(t1-t0))
logLine("Prediction time : {}".format(t2-t1))


out.close()

#########################################################


