import numpy as np

def gen_customerID():
    random_number = np.random.randint(100000, 999999)
    user_id = f'U{random_number}'
    return user_id