import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)
plt.figure(dpi = 300)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

import matplotlib.pyplot as plt

t = []
p2 = []
p3 = []

for i in range(0, 50, 2) :
    t.append(i / 10)
    p2.append((i / 10) ** 2)
    p3.append((i / 10) ** 3)
plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()



import numpy
print(numpy.sqrt(2)) #제곱근

import numpy as np
print(np.sqrt(2))

print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))

a = np.random.rand(5)
print(a)
print(type(a))

print(np.random.choice(6, 10))

print(np.random.choice(10, 6, replace = False)) # 비복원추출

print(np.random.choice(6, 10, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])) # p = 추출 확률

import matplotlib.pyplot as plt
import numpy as np

dice = np.random.choice(6, 10)
plt.figure(dpi = 300)
plt.hist(dice, bins = 6)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
dice = np.random.choice(6, 1000000, p=[0.1, 0.2, 0.3, 0.2, 0.1, 0.1])
plt.figure(dpi = 300)
plt.hist(dice, bins = 6)
plt.show()

import matplotlib.pyplot as plt
import random
dice = []
for i in range(1000000) :
    dice.append(random.randint(1,6))
plt.hist(dice, bins = 6)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 300)
a = np.random.randn(1000000)
plt.hist(a, bins = 1000)
plt.show()



a = np.array([1,2,3,4])
print(a)

print(a[1], a[-1])
print(a[1:])

a = np.array([1,2,'3',4]) # 하나가 문자열이면 모두가 문자열로 출력
print(a)

a = np.zeros(10)
print(a)

a = np.ones(10)
print(a)

a = np.eye(3) # 3 x 3의 단위 배열 생성
print(a)

import numpy as np
print(np.arange(3))
print(np.arange(3,7))
print(np.arange(3,7,2))

a = np.arange(1, 2, 0.1)
b = np.linspace(1, 2, 11)
print(a)
print(b)

a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20)
print(a)
print(b)

a = np.zeros(10) + 5
print(a)

a = np.linspace(1, 2, 11)
print(np.sqrt(a))

import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 300)
a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()

plt.figure(dpi = 300)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a + np.pi / 2, np.sin(a))
plt.show()

import numpy as np
a = np.arange(-5, 5)
print(a)

print(a < 0)

print(a[a < 0])

mask1 = abs(a) > 3 # 절댓값
print(a[mask1])

mask1 = abs(a) > 3
mask2 = abs(a) % 2 ==0
print(a[mask1 + mask2]) # 둘 중 하나의 조건이라도 참일 경우
print(a[mask1 * mask2]) # 두 가지 조건이 모두 참일 경우

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)

mask1 = abs(x) >50
mask2 = abs(y) >50
x = x[mask1 + mask2]
y = y[mask1 + mask2]

size = np.random.rand(len(x)) * 100 # 랜덤한 크기의 원을 x의 길이만큼 생성
plt.scatter(x, y, s = size, c = x, cmap = 'jet', alpha = 0.7)
plt.colorbar()
plt.show()

