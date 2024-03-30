import numpy as np

def gen_everyday_satisfaction():
  "Normal distribution with mean 3 and std 1.6"
  val = int(np.random.normal(loc=3, scale=1.6))
  while val < 1 or val > 5: # prevent values out of range
    val = int(np.random.normal(loc=3, scale=1.6))
  return val
  #TODO: find probability from other parameters such as living situation and age


def gen_health(mean=3, std=1, skewness=0):
    values = np.arange(1, 6)
    z_scores = (values - mean) / std
    probabilities = np.exp(-0.5 * z_scores**2) * (1 + skewness * z_scores)
    probabilities /= np.sum(probabilities)

    # ensure that all probabilities are non-negative
    if np.any(probabilities < 0):
        probabilities[probabilities < 0] = 0
        probabilities /= np.sum(probabilities)
    else:
        probabilities /= np.sum(probabilities)

    return np.random.choice(values, p=probabilities)