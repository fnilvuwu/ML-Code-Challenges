
import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)

    magnitude = np.linalg.norm(v1) * np.linalg.norm(v2)

    result = round(dot_product/magnitude, 3)
    return result

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))
v1 = np.array([1, 2, 3])
v2 = np.array([-1, -2, -3])
print(cosine_similarity(v1, v2))
v1 = np.array([1, 0, 7])
v2 = np.array([0, 1, 3])
print(cosine_similarity(v1, v2))