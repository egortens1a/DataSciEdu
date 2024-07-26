import numpy as np


def construct_matrix(x, y):
    return np.vstack(np.array([x, y])).reshape((4, 2))
