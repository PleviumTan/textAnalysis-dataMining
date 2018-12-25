dataList = []
import csv
import random
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

group = {"group A": 1, "group B": 2, "group C": 3, "group D": 4, "group E": 5}
educationL = {"some high school": 1, "high school": 2, "some college": 3, "associate\'s degree": 4,
              "bachelor\'s degree": 5, "master\'s degree": 6}
sex = {"famale": 0, "male": 1}
lunch = {"standard": 1, "free/reduced": 0}
pre={"none":0,"complate":1}
with open('StudentsPerformance.csv', 'r', encoding='iso-8859-1') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if (not count):
            count += 1
            continue
        newrow = [0, 0, 0, 0, 0]
        newrow[0] = sex[row[0]]

        newrow[1] = group[row[1]]

        newrow[2] = educationL[row[2]]

        newrow[3] = lunch[row[3]]

        newrow[4]=pre[row[4]]
        dataList.append([newrow, int(row[5])])

count = {'A': 0, 'B': 0, 'C': 0}
for student in dataList:
    if student[1] >= 240:
        student[1] = 2
        count['A'] += 1
    elif student[1] > 165:
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

clf = tree.DecisionTreeClassifier(splitter='best', max_depth=3)
clf = clf.fit(train_x, train_y)

print(clf.score(test_x, test_y))
