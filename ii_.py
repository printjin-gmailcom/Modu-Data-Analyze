import csv
f = open('seoul.csv', 'r', encoding='cp949') #인코딩 = 윈도우 한글 인코딩 방식
data = csv.reader(f, delimiter=',') # ',' 기준 분리 저장
print(data)
f.close()

import csv
f = open('seoul.csv', 'r', encoding='cp949')
data = csv.reader(f)
for row in data :
    print(row)
f.close()

import csv
f =open('seoul.csv')
data = csv.reader(f)
header =next(data) # 헤더 변수에 헤더 데이터행 저장 #next() ; 첫번째 데이터 행을 읽으면서 데이터의 탐색 위치를 다음 줄로 이동시키는 명령
print(header)
f.close()

import csv
f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
for row in data :
    print(row)
f.close()
