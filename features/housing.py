import numpy as np

#TODO: Check correlation with age for civilstånd, utbildningsnivå etc.

def gen_marital(age):
  if age < 18: return 6
  if age <= 25: np.random.choice([1, 5, 6], p=[0.01, 0.98, 0.01])
  if age >= 50: np.random.choice([1, 2, 3, 4, 5, 6,], p=[0.5, 0.05, 0.15, 0.15, 0.10, 0.05])
  return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.35, 0.02, 0.09, 0.04, 0.47, 0.03])
  # TODO: age should clearly be a used more thoughtful

def gen_accommodation():
  return np.random.choice([1, 2, 3, 4, 5], p=[0.25, 0.25, 0.49, 0.005, 0.005])
  # VERY ROUGH estimate, probably not even remotely close to actual distribution
  # TODO: add parameters for probability from age and other stuff

def gen_living_with(age, civilstånd):
  if age <= 17: return 4 # Garanterar boende med förälder under 17
  if age >= 31 or age <= 50: return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.2, 0.1, 0.2, 0.002, 0.002, 0.496]) # ökad sannolikhet att bo med familj i åldersspann 31-50
  if civilstånd == 2 or 3: return np.random.choice([1, 3, 5], p=[0.98, 0.01, 0.01])
  return np.random.choice([1, 2, 3, 5, 6], p=[0.362, 0.4, 0.02, 0.1, 0.118]) # ensamboende speglar scb 2019, resten lekmannaestimering