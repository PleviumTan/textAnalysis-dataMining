'''
不要改CSV文件，以我的为准
'''

dataList = []
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
import pydotplus

group = {"group A": 1, "group B": 2, "group C": 3, "group D": 4, "group E": 5}
educationL = {"some high school": 1, "high school": 2, "some college": 3, "associate\'s degree": 4,
              "bachelor\'s degree": 5, "master\'s degree": 6}
sex = {"female": 0, "male": 1}
lunch = {"standard": 1, "free/reduced": 0}
pre={"none":0,"completed":1}
def readData():
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

    count = {'A': 0, 'B': 0}
    for student in dataList:
        if student[1] >= 240:
            student[1] = 1
            count['A'] += 1
        else:
            student[1] = 0
            count['B'] += 1

    random.shuffle(dataList)
    return dataList

def decisionTree(dataList):
    train_x = [a[0] for a in dataList[:800]]
    train_y = [a[1] for a in dataList[:800]]
    test_x = [a[0] for a in dataList[800:]]
    test_y = [a[1] for a in dataList[800:]]

    clf = tree.DecisionTreeClassifier(random_state = 9,max_depth=4)
    clf = clf.fit(train_x, train_y)

    print(clf.score(test_x, test_y))

    dot_data = tree.export_graphviz(clf, out_file=None,filled=True, rounded=True, special_characters=True,class_names=['B','A'])
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("tree.pdf")

def studentClustering(dataList):
    #需要降维数据
    studentList = [a[0] for a in dataList]
    km = KMeans(init='k-means++', n_clusters=4)
    result = km.fit(studentList)
    label_pred = result.labels_#获取聚类标签
    centroids = result.cluster_centers_#获取聚类中心
    interia = result.inertia_#获取聚类准则的总和
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    #这里'or'代表中的'o'代表画圈，'r'代表颜色为红色，后面的依次类推
    color = 0
    j = 0
    student = np.array(studentList)
    for i in label_pred:
        plt.plot([student[j:j+1,0]], [student[j:j+1,1]], mark[i], markersize = 5)
        j +=1
    plt.show()
    return result



if __name__ == '__main__':
    dataList = readData()
    cluster = studentClustering(dataList)
    print(cluster.labels_)
