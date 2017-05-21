#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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


outputFile = "output2.txt"
out = open(outputFile, "w")

def logLine(line):
    out.write(line)
    out.write("\n")
    print line


#########################################################
### your code goes here ###

logLine("No of Features = {}".format(len(features_train[0])))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

clf = DecisionTreeClassifier(min_samples_split=40)

t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
labels_predict = clf.predict(features_test)
t2 = time()
accuracy = accuracy_score(labels_test, labels_predict)

logLine("Training with decision tree default values, min_sample_split = 40")
logLine("Accuracy : {}".format(accuracy))
logLine("Training time : {}".format(t1-t0))
logLine("Prediction time : {}".format(t2-t1))


#########################################################


out.close()
