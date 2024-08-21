import numpy as np

my_array = np.array([[1, 2],
                     [1, 4],
                     [5, 6]])

result = np.min(my_array, axis=1)
print(result.tolist())