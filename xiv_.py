import csv
f =open('age.csv')
data = csv.reader(f)
next(data)  # 헤더 제거
for row in data :
    print(row)

import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
home = []
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        for i in row[3:] :
            home.append(int(i))
print(home)

import numpy as np
import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype = int)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)
plt.rc('font', family ='Malgun Gothic')
plt.title(name +' 지역의 인구 구조')

plt.plot(home)
plt.show()

import numpy as np
import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype =int) / int(row[2])

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)
plt.rc('font', family ='Malgun Gothic')
plt.title(name +' 지역의 인구 구조')

plt.plot(home)
plt.show()

import numpy as np
import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype =int) / int(row[2])
for row in data :
    print(row)

import numpy as np
import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype =int) / int(row[2])
for row in data :
    away = np.array(row[3:], dtype = int) / int(row[2])
    print(home - away)

import numpy as np
import csv
f =open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype =int) / int(row[2])
for row in data :
    away = np.array(row[3:], dtype = int) / int(row[2])
    print(np.sum(home - away))

import numpy as np
import csv
f = open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype = int) / int(row[2])
    for row in data :
        away = np.array(row[3:], dtype = int) / int(row[2])
        s = np.sum(home - away)
        if s < mn :
            mn = s
            result_name = row[0]
            result = away

import matplotlib.pyplot as plt
plt.plot(home)
plt.plot(result)
plt.show()



import numpy as np
import csv

f =open('age.csv')
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn =1
result_name =''
result =0
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype =int) /int(row[2])
for row in data :
    away = np.array(row[3:], dtype =int) /int(row[2])
    s = np.sum((home - away) **2)
    if s < mn and name not in row[0] :
        mn = s
        result_name = row[0]
        result = away
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.figure(figsize = (10,5), dpi=300)
plt.rc('font', family ='Malgun Gothic')
plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label = name)
plt.plot(result, label = result_name)
plt.legend()
plt.show()

