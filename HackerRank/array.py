import numpy as np

def arrays(arr):
    return np.array([float(i) for i in arr][::-1], float)

print(arrays([1.1 ,-1.2]))