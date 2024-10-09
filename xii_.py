import csv
f = open('subwaytime.csv')
data = csv.reader(f)
for row in data :
    print(row)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
for row in data :
    row[4:] = map(int, row[4:]) # map(적용시킬 함수, 적용할 값들)
    print(row)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:] = map(int, row[4:])
    result.append(row[10])
print(len(result))
print(result)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:] = map(int, row[4:])
    result.append(row[10])
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:] = map(int, row[4:])
    result.append(row[10])
import matplotlib.pyplot as plt
result.sort() # 오름차순
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []
for row in data :
    row[4:] = map(int, row[4:])
    result.append(sum(row[10:15:2]))
import matplotlib.pyplot as plt
result.sort()
plt.style.use('ggplot')
plt.bar(range(len(result)), result)
plt.show()

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
for row in data :
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx :
        mx = sum(row[10:15:2])
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
for row in data :
    row[4:] = map(int, row[4:])
    a = row[11:16:2]
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = 0
mx_station = ''
t = int(input('몇 시의 승차인원이 가장 많은 역이 궁금하세요? : '))
for row in data :
    row[4:] = map(int, row[4:])
    a = row[2 * t - 4]
    if a > mx :
        mx = a
        mx_station = row[3] + '(' + row[1] + ')'
print(mx_station, mx)

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24
for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        a = row[j * 2 + 4]
        if a > mx[j] :
            mx[j] = a
            mx_station[j] = row[3]
print(mx_station)
print(mx)

import matplotlib.pyplot as plt
plt.rc('font', family ='Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation =90) # xticks
plt.show()

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24
for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        a = row[j * 2 + 4]
        if a > mx[j] :
            mx[j] = a
            mx_station[j] = row[3]+'('+str(j+4)+')'
import matplotlib.pyplot as plt
plt.rc('font',family = 'Malgun Gothic')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()

import csv
import matplotlib.pyplot as plt
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24
for row in data :
    row[4:] = map(int, row[4:])
    for j in range(24) :
        b = row[5 + j * 2]
        if b > mx[j] :
            mx[j] = b
            mx_station[j] = row[3]+'('+str(j+4)+')'
plt.rc('font',family = 'Malgun Gothic')
plt.bar(range(24), mx, color = 'b')
plt.xticks(range(24), mx_station, rotation = 90)
plt.show()

import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
s_in = [0] * 24
s_out = [0] * 24
for row in data :
    row[4:] = map(int, row[4:])
    for i in range(24) :
        s_in[i] += row[4 + i * 2]
        s_out[i] += row[5 + i * 2]
import matplotlib.pyplot as plt
plt.figure(dpi = 300)
plt.rc('font', family = 'Malgun Gothic')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label = '승차')
plt.plot(s_out, label = '하차')
plt.legend()
plt.xticks(range(24), range(4,28))
plt.show()

