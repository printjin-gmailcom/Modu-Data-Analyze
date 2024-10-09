import csv

f = open('age.csv')
data = csv.reader(f)

for row in data :
    print(row)

if '서울특별시 구로구 신도림동(1153051000)' == row[0] :
    print(row)

print('신도림' in '서울특별시 구로구 신도림동(1153051000)')
print('1153' in '서울특별시 구로구 신도림동(1153051000)')
print('()' in '서울특별시 구로구 신도림동(1153051000)')

import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    if '신도림' in row[0] :
        print(row)

import csv
f = open('age.csv')
data = csv.reader(f)

for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            print(i)

import csv
f = open('age.csv')
data = csv.reader(f)
result = []
for row in data :
    if '신도림' in row[0] :
        for i in row[3:] :
            result.append(int(i)) # 정수로 저장
print(result)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(result)
plt.show()

