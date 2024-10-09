import csv
f = open('age.csv')
data = csv.reader(f)
result = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.title(name +' 지역의 인구 구조')
plt.plot(result)
plt.show()

import matplotlib.pyplot as plt
plt.bar([0,1,2,4,6,10], [1,2,3,5,6,7]) # 막대를 표시할 위치, 막대의 높이
plt.show()

import matplotlib.pyplot as plt
plt.bar(range(6), [1,2,3,5,6,7])
plt.show()

import csv
f = open('age.csv')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.bar(range(101), result)
plt.show()

import csv
f = open('age.csv')
data = csv.reader(f)

result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i))

import matplotlib.pyplot as plt
plt.barh(range(101), result)
plt.show()



import csv
f = open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if '신도림' in row[0] :
        for i in range(0,101) :
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))
f.reverse()

import csv
f =open('gender.csv')
data = csv.reader(f)
m = []
f = []
for row in data :
    if'신도림'in row[0] :
        for i in row[3:104] :
            m.append(-int(i))
        for i in row[106:] :
            f.append(int(i))

import matplotlib.pyplot as plt
plt.barh(range(101), m)
plt.barh(range(101), f)
plt.show()

import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title('신도림 지역의 남녀 성별 인구 분포')
plt.barh(range(101), m, label = '남성')
plt.barh(range(101), f, label = '여성')
plt.legend()
plt.show()

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

