import numpy as np
import datetime

def gen_email(name, age):
  
  # 15% to spell name incorrectly in email (boomer factor)
  if age > 59 and np.random.choice([0, 1], p=[0.85, 0.15]):
    spelling_mistake(name)

  # add birth year to end of mail
  birth_year = datetime.date.today().year - age

  domän = np.random.choice(['gmail.com', 'hotmail.com',
                            'live.se', 'live.com', 'outlook.com',
                            'yahoo.se', 'icloud.com'],
                            p=[0.55, 0.05, 0.05, 0.05, 0.19, 0.01, 0.1])

  # 50% to have older domain if age > 60
  if age > 60 and np.random.randint(2) == 1:
      if np.random.randint(2) ==1: suffix = str(birth_year)[-2:] # 50% to remove first two digits from birth year
      domän = np.random.choice(['telia.se', 'spray.se', 'glocalnet.se', 'bredband.net', 'regeringen.se'],
      p=[0.30, 0.23, 0.23, 0.23, 0.01])

  # 90% to remove century from birth year if age < 60
  elif age < 60:
      if np.random.choice([0,1], p=[0.1, 0.9]) == 1: suffix = str(birth_year)[-2:]

  # 50% to remove entire birth year 25% to add a random int instead
  suffix_modifier = np.random.choice([0,1,3], p=[0.5, 0.25, 0.25])

  if suffix_modifier == 0: suffix = ''
  elif suffix_modifier == 1: suffix = np.random.randint(1,9)
  else: suffix = str(birth_year)[-2:]

	# 50% to have a first name "nickname", then 20% to only have first letter and .
  if np.random.choice([0,1], p=[0.5,0.5]) == 1:
    # TODO: there should be some mapping for this to determine likely ways to shorten names

    first, last = name.split()[0], name.split()[1]
    # If length > 7, only use first 3 letters
    if len(first) > 7:
      first = first[:3:]
    # if length > 6 only use first 4 letters 
    if len(first) > 6:
      first = first[:4:] 

    # 20% to have only first letter in first name
    if np.random.choice([0,1], p=[0.8, 0.2]) == 1:
      first, last = name.split()[0], name.split()[1]
      first = first[:1:] + np.random.choice(['_','.'])
    
    name = first + last



  # replace blank space and make lowercase
  x = np.random.choice(['_','__','-','.',''],p=[0.1,0.1,0.2,0.1,0.5])
  name = name.lower().replace(' ',x )

  # 10% to add other characters to email
  if np.random.choice([0,1], p=[0.9, 0.1]) == 1:
    prefix = '_'
  else:
    prefix = ''
  

  ################### Replace name entirely #####################

  # 5% to have a millenial email if millenial
  if birth_year in range(1989,1998) and np.random.choice([0,1], p=[0.95, 0.05]) == 1:
    return millenial_mail(birth_year)

  # 0.5% to have a completely random and anonymous email
  if np.random.choice([0,1], p=[0.995, 0.005]) == 1:
    return anonymize_mail1(is_apple=False) + '@' + domän

  # 1% to have an email hidden by apple services
  if np.random.choice([0,1], p=[0.99, 0.01]) == 1:
    return anonymize_mail1(is_apple=True)

  # 0.5% to have an "asdf" (when users just type "randomly") email:
  if np.random.choice([0,1], p=[0.995, 0.005]) == 1:
    return asdf_mail() + '@' + domän

  ################################################################
      
  return str(prefix) + str(name)+ str(suffix) + '@' + domän


## --- Misc stuff for mail --- ##

def anonymize_mail1(is_apple):
  length = np.random.randint(8, 12)
  chars = np.array(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
  if is_apple == True: return ''.join(np.random.choice(chars, size=10)) + '@privaterelay.appleid.com'
  return ''.join(np.random.choice(chars, size=length))

def asdf_mail():
	randy = np.random.choice([0,1,2])
	n = np.random.randint(1,9)

	if randy == 0: # The asdf:er
		chars = ['asdf','ddasff','assd','fffasas', 'asdasdf', 'asdasdasd']
		return (np.random.choice(chars)[-n:] + (np.random.choice(chars)[-n:]))

	elif randy == 1: # The "aaaaaa":er
		a = np.random.choice(['a','w','e','q'])
		return np.random.choice([a * n, a * (n+n)])

	else: # The obnoxious
		return np.random.choice(['bajs', 'jajajaja', 'dinmamma', 'kkk'])

def spelling_mistake(name):
    # Shuffles last and next to last letter of first name
    s = name.split()[0],
    i = len(s)-1
    j = len(s)-2
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return(''.join(s_list) + name.split()[1])

def millenial_mail(birth_year):
	deco = np.random.choice(['xX_', '_', '', ''])
	word_list1 = ['star', 'cool', 'dark', 'moon', 'knight', 'hunter']
	word_list2 = ['boy', 'girl', 'dude', 'killer', 'fire', 'master']
	separator = ['_', '', '', '-']
	domain_mil = '@' + np.random.choice(['gmail.com','live.com','live.se'])	
	stupid_mail = str(deco) + word_list1[np.random.randint(len(word_list1))] + separator[np.random.randint(len(separator))] + word_list2[np.random.randint(len(word_list2))] + str(deco[::-1])
	if stupid_mail[-1::] == 'x':
	  return stupid_mail + domain_mil
	return stupid_mail + str(birth_year)[-2:] + domain_mil