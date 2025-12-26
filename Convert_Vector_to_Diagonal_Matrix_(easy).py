import numpy as np

def make_diagonal(x):
    # Your code here
    result = []
    for i in range(len(x)):
        result.append([0]*i + [x[i]] + [0]*(len(x)-i-1))
    return result
    
print(make_diagonal(np.array([1, 2, 3])))
print(make_diagonal(np.array([4, 5, 6, 7])))