import pandas as pd
df = pd.read_html('https://ko.wikipedia.org/wiki/%EC%98%AC%EB%A6%BC%ED%94%BD_%EB%A9%94%EB%8B%AC_%EC%A7%91%EA%B3%84')
print(df)

import pandas as pd
df = pd.read_html('https://ko.wikipedia.org/wiki/%EC%98%AC%EB%A6%BC%ED%94%BD_%EB%A9%94%EB%8B%AC_%EC%A7%91%EA%B3%84')
df[1]

import pandas as pd
df = pd.read_html('https://ko.wikipedia.org/wiki/%EC%98%AC%EB%A6%BC%ED%94%BD_%EB%A9%94%EB%8B%AC_%EC%A7%91%EA%B3%84', header=0, index_col = 0)
df[0]

summer = df[0].iloc[:,:5]
summer

summer.columns = ['하계참가횟수','금','은','동','계']
summer

import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header = 0, index_col = 0)
summer = df[0].iloc[:,:5]
summer.columns = ['하계참가횟수','금','은','동','계']
summer.sort_values('금', ascending=False)

summer.to_excel('하계올림픽메달.xlsx')



import pandas as pd
index = pd.date_range('1/1/2000', periods =8)
print(index)

import numpy as np
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
df

import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
print(df['B'])

import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
print(df['B'] > 0.4)

df2 = df[df['B'] > 0.4]
df2

df3 = df2.T
df3

import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
df['D'] = df['A'] / df['B']
df

import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis = 1)
df.head()

import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis = 1)
df = df.sub(df['A'], axis =0)
df.head()

import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods =8)
df = pd.DataFrame(np.random.rand(8,3), index = index, columns = list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis = 1)
df = df.sub(df['A'], axis =0)
df = df.div(df['C'], axis = 0)
df.to_csv('test.csv')
df.head()



import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col = 0)
df.head()

import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col = 0)
df = df.div(df['총인구수'], axis =0)     # 비율로 변환
del df['총인구수'], df['연령구간인구수']  # 총인구수, 연령구간인구수 열 삭제

name = input('원하는 지역의 이름을 입력해주세요 : ')
a = df.index.str.contains(name)
df2 = df[a]
df2

import matplotlib.pyplot as plt
plt.rc('font', family ='Malgun Gothic')
df2.T.plot()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family ='Malgun Gothic')
df = pd.read_csv('age.csv', encoding='cp949', index_col = 0)
df = df.div(df['총인구수'], axis = 0)
del df['총인구수'], df['연령구간인구수']
name = input('원하는 지역의 이름을 입력해주세요 : ')
a = df.index.str.contains(name)
df2 = df[a]
df.loc[np.power(df.sub(df2.iloc[0], axis = 1), 2).sum(axis = 1).sort_values().index[:5]].T.plot()
plt.show()

