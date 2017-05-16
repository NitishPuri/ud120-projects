#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


def printPerson(personName):
	print "Data for %s :: BEGIN " % personName
	for data in enron_data[personName]:
		print "%s : %s" % (data, enron_data[personName][data]) 
	print "Data for %s :: END" % personName

def noOfPOI():
    no_of_poi = 0
    for person in enron_data:
        # print person
        if(enron_data[person]["poi"]==1):
            no_of_poi+=1
    print "Number of POI in dataset : %d " % no_of_poi

def quantifiedSalary():
    count = 0
    for person in enron_data:
        if(enron_data[person]["salary"] != 'NaN'):
            count+=1
    print "Number of people with quantified salary : %d " % count

def knownEmailAddress():
    count = 0
    for person in enron_data:
        if(enron_data[person]["email_address"] != 'NaN'):
            count+=1
    print "Number of people with known email address : %d " % count

def totalPaymentsPercentage():
    count = 0
    for person in enron_data:
        if(enron_data[person]["total_payments"] == 'NaN'):
            count += 1
    print "Percentage of people with 'Nan' as total_payments : %f " % (count*100 / len(enron_data)) 

def poiTotalPaymentsPercentage():
    count = 0
    no_of_poi = 0
    for person in enron_data:
        if(enron_data[person]["poi"]==1):
            no_of_poi += 1
            if(enron_data[person]["total_payments"] == 'NaN'):
                count += 1
    print "Percentage of POI with 'Nan' as total_payments : %f " % (count*100 / no_of_poi) 


noOfPOI()
# quantifiedSalary()
# knownEmailAddress()
# totalPaymentsPercentage()
# poiTotalPaymentsPercentage()
# printPerson("SKILLING JEFFREY K")


