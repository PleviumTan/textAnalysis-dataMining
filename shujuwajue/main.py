dataList = []
import csv
import random
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

with open('StudentsPerformance.csv','r',encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if(not count):
            count += 1
            continue
        newrow = [0,0,0,0,0]
        if row[0] == 'female':
            newrow[0] = 0
        elif row[0] == 'male':
            newrow[0] = 1
        else:
            print('Gender value error')

        if row[1] == 'group A':
            newrow[1] = 1
        elif row[1] == 'group B':
            newrow[1] = 2
        elif row[1] == 'group C':
            newrow[1] = 3
        elif row[1] == 'group D':
            newrow[1] = 4
        elif row[1]== 'group E':
            newrow[1] = 5
        else:
            print('Ethnic value error')

        if row[2] =='some high school':
            newrow[2] = 1
        elif row[2] == 'high school':
            newrow[2] = 2
        elif row[2] == 'some college':
            newrow[2] = 3
        elif row[2] =='associate\'s degree':
            newrow[2] = 4
        elif row[2] == 'bachelor\'s degree':
            newrow[2] = 5
        elif row[2] == 'master\'s degree':
            newrow[2] = 6
        else:
            print('Degree value error')

        if row[3] == 'standard':
            newrow[3] = 1
        elif row[3] == 'free/reduced':
            newrow[3] =0
        else:
            print('Lunch value error')

        if row[4] == 'completed':
            newrow[4] = 1
        elif row[4] == 'none':
            newrow[4] = 0
        else:
            print('Course value error')
        dataList.append([newrow,int(row[5])])

count = {'A':0,'B':0,'C':0}
for student in dataList:
    if student[1]>=240:
        student[1] = 2
        count['A']+=1
    elif student[1]>165:
        student[1] = 1
        count['B'] += 1
    else:
        student[1] = 0
        count['C'] += 1


random.shuffle(dataList)

train_x = [a[0] for a in dataList[:800]]
train_y = [a[1] for a in dataList[:800]]
test_x = [a[0] for a in dataList[800:]]
test_y = [a[1] for a in dataList[800:]]

clf = tree.DecisionTreeClassifier(splitter = 'best',max_depth=3)
clf = clf.fit(train_x, train_y)

print(clf.score(test_x,test_y))
