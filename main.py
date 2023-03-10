import numpy as np
import pandas as pd
import os
import hashlib

import _email, bucket, mapping

# GDPR notice: this program can potentially generate real personal data
# Make sure anonymize is TRUE or manually check all generated rows before making anything public

anonymize = False

# Dir for exporting csv or xlsx
os.makedirs('Exports', exist_ok=True)  

# Adjust ammount of people / entries to generate
rows = 1000

# Adjust export settings
export_csv = False
export_excel = True
export_path = 'Exports'
file_name ='file_name'

#------------------------------------ TODO: ------------------------------------------ #

# I slutändan blir det här en tuple med ints som mappas till olika beskrivande namn (utbildning, boende, etc.)
# När fine-tuning av fördelningar kan anses vara färdig går det att formulera mycket enklare och kortare funktion
# för att med sannolikhetsfördelning generera ett nästintill identiskt resultat. 

# Namn (och email) ska 'tokenifieras', annars är all annan data nominaldata (i vissa fall ordinal) med små integers

# ------------------------------------------------------------------------------------ #

# Eftersom nb slumpas innan kvinna/man kan det totala värdet på inparametrar överstiga 1,
# Detta gäller inte för andra funktioner, där sum av alla fördelningar måste vara 1 från början
def gen_gender(kvinna=0.5, man=0.5, nb=0.02):
  if anonymize:
    return 3
  if np.random.uniform() < 1 - nb:
    return np.random.choice([1, 2], p=[1-kvinna, 1-man])
  else:
    return 3

def gen_age():
  "Normal distribution, mean of 42 and a standard deviation of 20"
  age = int(np.random.normal(loc=42, scale=20))
  while age <= 15 or age >= 100:
    age = int(np.random.normal(loc=42, scale=20))
  return age
  # There is probably a way to avoid having to write this twice while still using normal distribution, but it works for now
#TODO: Check correlation with age for civilstånd, utbildningsnivå etc.

def gen_civilstånd(age):
  if age <= 25: np.random.choice([1, 5, 6], p=[0.01, 0.98, 0.01])
  if age >= 50: np.random.choice([1, 2, 3, 4, 5, 6,], p=[0.5, 0.05, 0.15, 0.15, 0.10, 0.05])
  return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.35, 0.02, 0.09, 0.04, 0.47, 0.03])
  # TODO: age should clearly be a used more thoughtful

def gen_utbildningsnivå(age):
  if age <= 17: return 1 # Grundskolenivå garanterad för age <= 16
  elif age in range(18,19): return np.random.randint(1, high=3) # Slumpar studentexamen för 18-19 år
  elif age >= 19: return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.01, 0.01, 0.26, 0.21, 0.270, 0.24])
  # allt annat random TODO: implement probability for each age

def gen_sysselsättning(age):
  if age >= 66: return 5 # Garanterar pension över 66
  elif age >= 60: return np.random.choice([1, 4, 5, 6]) # Möjlig pension över 60, ej möjliga studier
  elif age <= 17: return 2 # Garanterar studier under 17
  elif age >= 18 or age <= 30: return np.random.choice([1, 2, 3, 4], p=[0.25, 0.65, 0.05, 0.05]) #Högre sannolikhet att vara student
  return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.7, 0.1, 0.088, 0.086, 0.0, 0.02]) # Speglar arbetslöshet och sjukskrivning i sverige 2022

def gen_boende():
  return np.random.choice([1, 2, 3, 4, 5], p=[0.25, 0.25, 0.49, 0.005, 0.005])
  # VERY ROUGH estimate, probably not even remotely close to actual distribution
  # TODO: add parameters for probability from age and other stuff

def gen_bor_med(age, civilstånd):
  if age <= 17: return 4 # Garanterar boende med förälder under 17
  if age >= 31 or age <= 50: return np.random.choice([1, 2, 3, 4, 5, 6], p=[0.2, 0.1, 0.2, 0.002, 0.002, 0.496]) # ökad sannolikhet att bo med familj i åldersspann 31-50
  if civilstånd == 2 or 3: return np.random.choice([1, 3, 5], p=[0.98, 0.01, 0.01])
  return np.random.choice([1, 2, 3, 5, 6], p=[0.362, 0.4, 0.02, 0.1, 0.118]) # ensamboende speglar scb 2019, resten lekmannaestimering

## ------- Health  ------- ##

def gen_vardagstillfredsställelse():
  "Normal distribution with mean 3 and std 1.6"
  val = int(np.random.normal(loc=3, scale=1.6))
  while val < 1 or val > 5: # prevent values out of range
    val = int(np.random.normal(loc=3, scale=1.6))
  return val
  #TODO: find probability from other parameters such as living situation and age

def gen_health():
  return np.random.choice([1,2,3,4,5], p=[0.05,0.2,0.5,0.2,0.05]) # lazy normal distribution

#TODO:
## ------ Daily/weekly time ------ #

# Arbete	Skötsel	Lek	Rekreation	Sömn
# Time should add up 1440 (24 hours)

# Tid_ensam	Tid_familj	Tid_vänner	Tid_övriga
# time does not have to add up to anything specific but sum cannot be > 1440 (24 hours)

## ------- Name & Contact ------ ##

def gen_name(gender):

  # TODO: conformist gender specific names + first, last name commonly matched

  # awful structure, TODO: optimize. actually no, the entire name generation shoud be rewritten
  if gender == 1:
    first_bucket = [bucket.f_norwa_list, bucket.f_scandi_gpt, bucket.f_slavic_gpt, bucket.f_sweden_gpt]
  elif gender == 2:  
    first_bucket = [bucket.m_scandi_gpt, bucket.m_slavic_gpt, bucket.m_sweden_gpt]
  elif gender == 3:
    first_bucket = [bucket.f_norwa_list, bucket.f_scandi_gpt, bucket.f_slavic_gpt, bucket.f_sweden_gpt, bucket.m_scandi_gpt, bucket.m_slavic_gpt, bucket.m_sweden_gpt]

  # Just a test set-up. This wouldn't be an issue, but it doesn't take cultural matching first and last names into calculations and is currently limited to some regional variations
  first_name = first_bucket[np.random.randint(0,len(first_bucket))]
  first_name = first_name[np.random.randint(0,len(first_name))]
  
  # Here maybe last names should be adjusted to match first names according to cultural status quo
  last_bucket = [bucket.last_gpt_asia, bucket.last_gpt_eur0, bucket.last_gpt_eur1, bucket.last_gpt_eur2, bucket.last_gpt_mena, bucket.last_swe]
  last_name = last_bucket[np.random.randint(0,len(last_bucket))]
  last_name = last_name[np.random.randint(0,len(last_name))]

  return first_name + ' ' + last_name

def gen_phone():
  # challenge# 1: needs to be unique
  # for now it will have a probability of 2.474631929433396e-07 to be duplicare
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

# Hashing for anonymization
def hash_string(string, end:int):
    sha256_hash = hashlib.sha256(string.encode())
    return sha256_hash.hexdigest()[::end]


def generate_person(): # should make a class (?)
    # Pure ints
    age = gen_age()
    phone = gen_phone()
    gendr = gen_gender()
    civil = gen_civilstånd(age)
    utbil = gen_utbildningsnivå(age)
    syssl = gen_sysselsättning(age)
    boend = gen_boende()
    bormd = gen_bor_med(age, civil)
    vardt = gen_vardagstillfredsställelse()
    hälsa = gen_health()

    # TODO: Token this
    name = gen_name(gendr)
    mail = _email.gen_email(name, age, anonymize)
    _psw = _email.gen_psw(name, age, anonymize)

    return (age,name,mail,_psw,phone,gendr,civil,utbil,syssl,boend,bormd,vardt,hälsa)

if __name__ == '__main__':
    
    # loop to generate rows
    person_list = [generate_person() for n in range(rows)]

    df = pd.DataFrame(person_list, columns=['Ålder','Namn', 'Email', 'Lösenord', 'Telefon', 'Kön', 'Civilstånd', 'Utbildningsnivå', 'Sysselsättning', 'Boende', 'Tillsammans_med', 'Vardagstillfredsställelse', 'Hälsa'])
    
    df['Kön'] = df['Kön'].map(mapping.kön_map)
    df['Civilstånd'] = df['Civilstånd'].map(mapping.civil_map)
    df['Utbildningsnivå'] = df['Utbildningsnivå'].map(mapping.utbil_map)
    df['Sysselsättning'] = df['Sysselsättning'].map(mapping.syssl_map)
    df['Boende'] = df['Boende'].map(mapping.boend_map)
    df['Tillsammans_med'] = df['Tillsammans_med'].map(mapping.bormd_map)

    if anonymize:
      print('Hashing selected columns')
      df['Namn'] = df['Namn'].apply(hash_string,end=8)

    print(df)
    if export_csv:
      pd.DataFrame.to_csv(df, export_path + '/' + file_name + '.csv')
    
    if export_excel:
      pd.DataFrame.to_excel(df, export_path + '/' + file_name + '.xlsx')