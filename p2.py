import matplotlib.pyplot as plt
import numpy as np

y = np.array([21.429, 10.714, 39.286, 21.429, 7.143])
SUB = ["Bio Tech", "Civil", "Mech", "ECE", "CSE"]
myexplode = [0, 0, 0, 0.2, 0.5]

plt.pie(y, labels = SUB, explode = myexplode, autopct='%1.1f%%')

plt.show()