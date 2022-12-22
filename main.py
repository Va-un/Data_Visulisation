import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame(np.random.rand(4, 4))
df.plot.bar()
plt.show()