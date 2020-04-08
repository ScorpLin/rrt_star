import numpy as np


def dist_between_points(a, b):
    """
    Return the Euclidean distance between two points
    :param a: first point
    :param b: second point
    :return: Euclidean distance between a and b
    """
    a = np.asarray(a)
    b = np.asarray(b)
    distance = np.linalg.norm(np.array(b) - np.array(a))
    return distance


def sample_uniform(prev_point):
    """return a state x that is sampled uniformly from the domain"""
    dimension = np.array([(-10, 10), (10, -10)])
    # p = index.Property()
    dim = dimension
    flag = False
    state = np.random.uniform(dim[:, 0], dim[:, 1])
    while flag is False:
        step = dist_between_points(state, prev_point)
        if step <= 1:
            flag = True
        else:
            state = np.random.uniform(dim[:, 0], dim[:, 1])
    return tuple(state)
