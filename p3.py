import matplotlib.pyplot as plt
import numpy as np

y = np.array([21, 22, 12, 8, 6, 23, 8])
S = ["Grocery","Automobile", "utility bill", "Dining out", "Health Care", "Saving", "other expenses"]
myexplode = [0, 0.2, 0, 0, 0, 0.1 ,0]

plt.pie(y, labels = S, explode = myexplode, autopct='%1.1f%%', shadow = True, startangle = 0)

plt.show()