import numpy as np

def gen_education(age):
  if age <= 17: return 1 # Grundskolenivå garanterad för age <= 16
  elif age in range(18,19): return np.random.randint(1, high=3) # Slumpar studentexamen för 18-19 år
  elif age >= 19: return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.01, 0.01, 0.26, 0.21, 0.270, 0.24])
  # allt annat random TODO: implement probability for each age

def gen_occupation(age):
  if age >= 66: return 5 # Garanterar pension över 66
  elif age >= 60: return np.random.choice([1, 4, 5, 6]) # Möjlig pension över 60, ej möjliga studier
  elif age <= 17: return 2 # Garanterar studier under 17
  elif age >= 18 or age <= 30: return np.random.choice([1, 2, 3, 4], p=[0.25, 0.65, 0.05, 0.05]) #Högre sannolikhet att vara student
  return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.7, 0.1, 0.088, 0.086, 0.0, 0.02]) # Speglar arbetslöshet och sjukskrivning i sverige 2022