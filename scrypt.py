import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

weekData = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

for i in range(1, 15):
    with open('gitStat{}.csv'.format(i), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if weekData[i-1].keys().__contains__(row[0]):
                weekData[i-1][row[0]][0] += int(row[1])
                weekData[i-1][row[0]][1] -= int(row[2])
            else:
                weekData[i-1][row[0]] = [int(row[1]), int(row[2])]

while weekData[0].items().__len__() == 0:
    weekData.append(weekData.pop(0))   

print(weekData)

users = ['clement.cardot', 'nicolas.moerman', 'augustin.baffou', 'maxime.kermagoret', 'alexis.bonamy', 'maxime.aumont', 'theo.saindrenan', 'marie.bordet']


additionData = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

deletionData = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]



for i in range(0, 14):
    for key in users:
        index = users.index(key)
        if weekData[i].keys().__contains__(key):
            additionData[i][index] += weekData[i][key][0]
            # Switch for cumulative data
            # for j in range(i, 15):
            #     additionData[j][index] += weekData[i][key][0]

for i in range(0, 14):
    for key in users:
        index = users.index(key)
        if weekData[i].keys().__contains__(key):
            deletionData[i][index] += weekData[i][key][1]
            # Switch for cumulative data
            # for j in range(i, 15):
            #     deletionData[j][index] += weekData[i][key][1]


df_add = pd.DataFrame(additionData, columns=users)
df_add.plot.area()
plt.title('Addition of lines of code per week')
plt.show()

df_suppr = pd.DataFrame(deletionData, columns=users)
df_suppr.plot.area()
plt.title('Deletion of lines of code per week')
plt.show()


