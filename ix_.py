import csv
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data :
    if name in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()

# > 제주특별자치도 입력시 - 'ValueError: shape mismatch: objects cannot be broadcast to a single shape'

print(len(m), len(f))

import csv
f = open('gender.csv')
data = csv.reader(f)

m = []
f = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data :
    if name in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))
        break # 문제 해결 방법

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + ' 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()



import matplotlib.pyplot as plt
plt.pie([10,20])
plt.show()

import matplotlib.pyplot as plt
size = [2441, 2312, 1031, 1233]
plt.axis('equal')
plt.pie(size)
plt.show()

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
plt.axis('equal')
plt.pie(size, labels = label, autopct = '%.1f%%')   # 비율 및 범례 추가
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
size = [2441, 2312, 1031, 1233]
label = ['A형','B형','AB형', 'O형']
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
plt.axis('equal')
plt.pie(size, labels = label, autopct = '%.1f%%', explode = (0,0,0.1,0), colors = color) # explode = 돌출
plt.legend()
plt.show()



import csv
f = open('gender.csv')
data = csv.reader(f)

size = []

name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
for row in data :
    if name in row[0] :
        m = 0
        f = 0
        for i in range(101) :
            m += int(row[i+3])
            f += int(row[i+106])
        break
size.append(m)
size.append(f)

import matplotlib.pyplot as plt
plt.rc('font', family ='Malgun Gothic')
color = ['crimson', 'darkcyan']
plt.axis('equal')
plt.pie(size, labels = ['남','여'], autopct ='%.1f%%', colors = color, startangle =90) # startangle - 파이의 시작 각도
plt.title(name + ' 지역의 남녀 성별 비율')
plt.show()

