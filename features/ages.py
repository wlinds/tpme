import numpy as np

def gen_age(mean=42, std=20, lower_lim=15, upper_lim=100):
  "Normal distribution, default mean of 42 and standard deviation of 20"

  # Probably a better solution
  age = int(np.random.normal(loc=mean, scale=std))
  age = max(age, lower_lim)
  age = min(age, upper_lim)
  return age
