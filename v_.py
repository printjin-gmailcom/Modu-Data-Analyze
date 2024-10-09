import csv

f = open('seoul.csv')
data = csv.reader(f)

for row in data :
    print(row)

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)

for row in data :
    print(row[-1])

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))
print(result)

print(len(result))

import csv
import matplotlib.pyplot as plt
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))

plt.plot(result, color = 'r')
plt.show()

import matplotlib.pyplot as plt
plt.figure(figsize = (10,2), dpi = 300) #가로10인치, 세로2인치
plt.plot(result, 'r')
plt.show()

s = 'hello python'
print(s)

date = '1907-10-01'
print(date.split('-'))

print(date.split('-')[0])
print(date.split('-')[1])
print(date.split('-')[2])

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08' :
            result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.plot(result, 'hotpink')
plt.show()

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
            result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.plot(result, 'hotpink')
plt.show()

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' :
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
            high.append(float(row[-1]))
            low.append(float(row[-2]))

import matplotlib.pyplot as plt
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' :
        if 2000 <= int(row[0].split('-')[0]) :
            if row[0].split('-')[1] == '12' and row[0].split('-')[2] == '15' :
                high.append(float(row[-1]))
                low.append(float(row[-2]))

import matplotlib.pyplot as plt
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.show()

import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' :
        if 1983 <= int(row[0].split('-')[0]) :
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
                high.append(float(row[-1]))
                low.append(float(row[-2]))

import matplotlib.pyplot as plt
#plt.figure(dpi = 300)
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')
plt.rc('font', family ='Malgun Gothic')
plt.title('내 생일의 기온 변화 그래프')
plt.show()

import csv
import matplotlib.pyplot as plt

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []
low = []

for row in data :
    if row[-1] != '' and row[-2] != '' :
        date = row[0].split('-')
        if 2000 <= int(date[0]) :
            if date[1] == '12' and date[2] == '15' :
                high.append(float(row[-1]))
                low.append(float(row[-2]))

                plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지
plt.title('내 생일의 기온 변화 그래프')
plt.plot(high, 'hotpink', label = 'high')

plt.plot(low, 'skyblue', label = 'low')
plt.legend()
plt.show()

