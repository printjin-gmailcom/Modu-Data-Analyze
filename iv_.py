import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40])
plt.show()

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [12, 43, 25, 15])
plt.show()

import matplotlib.pyplot as plt
plt.title('plotting')
plt.plot([10, 20, 30, 40])
plt.show()

import matplotlib.pyplot as plt
plt.title('legend')
plt.plot([10, 20, 30, 40], label ='asc') # 증가 = asc
plt.plot([40, 30, 20, 10], label ='desc') # 감소 = desc
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.title('color')
plt.plot([10, 20, 30, 40], color ='skyblue', label ='skyblue')
plt.plot([40, 30, 20, 10], color ='pink', label ='pink')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.title('linestyle')
plt.plot([10, 20, 30, 40], color ='r', linestyle ='--', label
='dashed')
plt.plot([40, 30, 20, 10], color ='g', ls =':', label ='dotted')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
plt.title('marker')
plt.plot([10, 20, 30, 40], 'r.', label ='circle') # r. = 점모양 마커
plt.plot([40, 30, 20, 10], 'g^', label ='triangle up') # g^ = 세모모양 마커
plt.legend() #범례
plt.show()

