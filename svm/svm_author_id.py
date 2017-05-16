#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


outputFile = "rbf5.txt"
out = open(outputFile, "w")

def logLine(line):
    out.write(line)
    out.write("\n")
    print line


#########################################################
### your code goes here ###

#########################################################

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

C = 10000.0
clf = SVC(kernel='rbf', C=C)
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]
t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
labels_predict = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(labels_test, labels_predict)

# logLine("Training on 1% data with rbf kernel. C = {}".format(C))
logLine("Training on full data with rbf kernel. C = {}".format(C))
logLine("Accuracy : {}".format(accuracy))
logLine("Training time : {}".format(t1-t0))
logLine("Prediction time : {}".format(t2-t1))
logLine("Predicion for 10 : {}".format(labels_predict[10]))
logLine("Predicion for 26 : {}".format(labels_predict[26]))
logLine("Predicion for 50 : {}".format(labels_predict[50]))
logLine("Chris emails {}".format(len([x for x in labels_predict if x == 1])))


out.close()

