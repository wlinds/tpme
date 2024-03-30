import numpy as np

def gen_gender(anonymize=False, female=0.5, male=0.5, nb=0.02):
    if anonymize:
        return 3
    if np.random.uniform() < 1 - nb:
        return np.random.choice([1, 2], p=[1-female, 1-male])
    else:
        return 3
