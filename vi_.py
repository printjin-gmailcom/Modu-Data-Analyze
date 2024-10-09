import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.plot(result, 'r')
plt.show()

import matplotlib.pyplot as plt
plt.hist([1,1,2,3,4,5,6,6,7,8,10])
plt.show()

import random
print(random.randint(1,6))

import random
for i in range(5) :
    print(random.randint(1,6))

import random
dice = []
for i in range(5) :
    dice.append(random.randint(1,6))
print(dice)

import random
dice = []
for i in range(5) :
    dice.append(random.randint(1,6))
print(dice)

import matplotlib.pyplot as plt
plt.hist(dice, bins = 6) # bin = 가로축의 개수
plt.show()

import random
dice = []
for i in range(100) :
    dice.append(random.randint(1,6))

import matplotlib.pyplot as plt
plt.hist(dice, bins = 6)
plt.show()

import random
dice = []
for i in range(100) :
    dice.append(random.randint(1,6))

import matplotlib.pyplot as plt
plt.hist(dice, bins = 6)
plt.show()

import random
dice = []
for i in range(1000000) :
    dice.append(random.randint(1,6))

import matplotlib.pyplot as plt
plt.hist(dice, bins = 6)
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.hist(result, bins = 100, color = 'r')
plt.show()

plt.figure(dpi = 300)
plt.hist(result, bins = 1000, color = 'r')
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.hist(aug, bins = 100, color = 'r')
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.hist(aug, bins = 100, color = 'r', label = 'Aug')
plt.hist(jan, bins = 100, color = 'b', label = 'Jan')
plt.legend()
plt.show()

import matplotlib.pyplot as plt

import random
result = []
for i in range(13) :
    result.append(random.randint(1,1000))
print(sorted(result))

plt.boxplot(result)
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
result = []

for row in data :
    if row[-1] != '' :
        result.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot(result)
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot(aug)
plt.boxplot(jan)
plt.show()

import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '' :
        if month == '08':
            aug.append(float(row[-1]))
        if month == '01':
            jan.append(float(row[-1]))

import matplotlib.pyplot as plt
plt.boxplot([aug,jan])
plt.show()

import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)
month = [[],[],[],[],[],[],[],[],[],[],[],[]]

for row in data :
    if row[-1] != '' :
        month[int(row[0].split('-')[1])-1].append(float(row[-1]))

plt.boxplot(month)
plt.show()

import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = []
for i in range(31) :
    day.append([])

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.boxplot(day, showfliers=False) # 아웃라이어 생략
plt.show()

import matplotlib.pyplot as plt
import csv
f = open('seoul.csv')
data = csv.reader(f)
next(data)

day = [[] for i in range(31)]

for row in data :
    if row[-1] != '' :
        if row[0].split('-')[1] == '08':
            day[int(row[0].split('-')[2])-1].append(float(row[-1]))

plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.boxplot(day, showfliers=False)
plt.show()

