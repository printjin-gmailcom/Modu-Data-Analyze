import csv
f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
for row in data :
    row[-1] = float(row[-1]) # 실수로 변경
    print(row)
f.close()

import csv
max_temp =-999   # 최고 기온 값
max_date =''
f =open('seoul.csv')
data = csv.reader(f)
header =next(data)
for row in data :
    if row[-1] =='' :
        row[-1] =-999   # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    if max_temp < row[-1] :
        max_date = row[0]
        max_temp = row[-1]
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로, ', max_temp, '도 였습니다.')

