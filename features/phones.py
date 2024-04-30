import numpy as np

def gen_phone(anonymize=False):
    # challenge# 1: needs to be unique
    # for now it will have a probability of 2.474631929433396e-07 to be duplicare

    # Swedish phone# TODO add other 
    a = str(np.random.choice([70, 72, 73, 76, 79]))
    b = np.random.randint(100, high=999)
    c = np.random.randint(100, high=999)

    if anonymize:
        a = 'XX'

    def add_zero(n):
        if n < 10: n = '00' + str(n)
        elif n < 100: n = '0' + str(n)
        return str(n)

    phone = str(0) + a + str(np.random.randint(0,9)) + add_zero(b) + add_zero(c)
    return phone