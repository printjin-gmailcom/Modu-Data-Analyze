import csv
f = open('subwayfee.csv')
data = csv.reader(f)

for row in data :
    print(row)

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    rate = row[4] / row[6] #division by zero 발생
    if rate > mx :
        mx = rate
print(mx)

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] == 0 :
        print(row)

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 :
        rate = row[4] / row[6]
        if rate > mx :
            mx = rate
            print(row, round(rate,2)) # (row, round(rate,2)) - 소수점 둘째자리까지 반올림

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            print(row, round(rate,2))

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > 0.94 :
            mx = rate
            print(row, round(rate,2))

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1]

print(mx_station, round(mx * 100,2))



import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = [0] * 4
mx_station = [''] * 4

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]

for i in range(4) :
    print(mx_station[i], mx[i])

import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]
for i in range(4) :
    print(label[i] + ' : ' + mx_station[i], mx[i])



import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.pie(row[4:8])
    plt.axis('equal')
    plt.show()

import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family = 'Malgun Gothic')
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi = 300)
    plt.title(row[3] + ' ' + row[1])
    plt.pie(row[4:8], labels = label, colors = c, autopct = '%1.f%%') #%1.f%% - 소수점 미출력
    plt.axis('equal')
    plt.show()

import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
plt.rc('font', family = 'Malgun Gothic')
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi = 300)
    plt.title(row[3] + ' ' + row[1])
    plt.pie(row[4:8], labels = label, colors = c, autopct = '%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3] + ' ' + row[1] + '.png') # plt.savefig - 이미지 파일로 저장
    plt.show()

