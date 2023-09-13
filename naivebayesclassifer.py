import numpy as np
import math 
import csv

def read(filename):
    with open(filename,'r') as f:
        dat = csv.reader(f)
        data = list(dat)
    metadata = data[0]
    traindata = data[1:]
    return metadata,traindata

def splitdata(dataset,splitratio):
    trainsize = int(len(dataset)*splitratio)
    trainset = []
    testset = list(dataset)
    while len(trainset)<trainsize:
        trainset.append(testset.pop(0))
    return [trainset,testset]

def classify(data,test):
    totalsize = data.shape[0]

    countyes =countno = probyes=probno=0
    for x in range(data.shape[0]):
        if data[x,data.shape[1]-1]=='Yes':
            countyes+=1
        else:
            countno+=1
    probyes = countyes/data.shape[0]
    probno = countno/data.shape[0]

    prob0=np.zeros((test.shape[1]-1))
    prob1=np.zeros((test.shape[1]-1))


    accuracy = 0
    for t in range(test.shape[0]):
        for k in range(test.shape[1]-1):
            count0=count1=0
            for j in range(data.shape[0]):
                if test[t,k]==data[j,k] and data[j,data.shape[1]-1]=='No':
                    count0+=1
                else:
                    count1+=1
            prob0[k]=count0/countno
            prob1[k]=count1/countyes
        prno = probno
        pryes= probyes
        for i in range(test.shape[0]):
            prno=prno*prob0[i]
            pryes=pryes*prob1[i]
        if prno>pryes:
            predict='No'
        else:
            predict='Yes'

        if predict==test[t,test.shape[1]-1]:
            accuracy+=1
    print(accuracy)


metadata,traindata = read('enjoysport.csv')


trainset,testset = splitdata(traindata,0.7)

train = np.array(trainset)
test = np.array(testset)
classify(train , test)
