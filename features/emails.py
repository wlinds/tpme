import numpy as np
import datetime
import re
import pickle


def gen_email(name: str = None, 
              age: int = None,
              anonymize: bool = 0,

              add_birth_p = [0.5, 0.25, 0.25],

              boomer_age: int = 59,
              boomer_factor: float = 0.15,
              
              domain_distribution: list = [0.55, 0.05, 0.05, 0.05, 0.19, 0.01, 0.1],
              force_domain: str = "",
              
              century_removal_p: float = 0.9,
              nickname_p: float = 0.5,

              mean_age: int = 40,
              std_age: int = 15,

              millenial_mail_p: float = 0.05,
              anonymize_mail_p: float = 0.005,
              apple_hidden_p: float = 0.01,
              asdf_mail_p: float = 0.05,

              force_formal: bool = False,

              allow_foreign_characters = False,
              
              ):

    if not name:
      try:
          file_path = 'Data/name_corpus.pkl'
          with open(file_path, 'rb') as file:
              name_corpus = pickle.load(file)

          name_dict_keys = list(name_corpus.keys())
          name = np.random.choice(name_corpus[np.random.choice(name_dict_keys)] + name_corpus[np.random.choice(name_dict_keys)])
          name += " " + np.random.choice(name_corpus[np.random.choice(name_dict_keys)])
          # TODO This is too random. Should be replaced with the function that generates names from tokens.

      except FileNotFoundError:
          print(f"Name generation error: Could not find {file_path}. Name set to default.")
          name = "John Doe"

    if not allow_foreign_characters:
        name = re.sub(r'[^a-zA-Z0-9 ]', '_', name)
        # name = name.replace('å', 'a').replace('ö', 'o').replace('ä', 'a')

    if not age:
        age = int(np.random.normal(mean_age, std_age))

    # TODO handle domain better
    domain_bucket = ['gmail.com', 'hotmail.com', 'live.se', 'live.com', 'outlook.com', 'yahoo.se', 'icloud.com']
    other_domains = ['telia.se', 'spray.se', 'glocalnet.se', 'bredband.net', 'regeringen.se']

    if force_domain != "":
        domain_distribution = [1]
        domain_bucket = [force_domain]
        other_domains = [force_domain]

    if force_formal and force_domain:
        return f"{name.split()[0].lower()}.{name.split()[1].lower()}@{force_domain}"

    if age > boomer_age and np.random.rand() < boomer_factor:
        pass # name = spelling_mistake(name.split()[0])

    birth_year = datetime.date.today().year - age # Add birth year to end of mail 
    mail_domain = np.random.choice(domain_bucket, p=domain_distribution)

    if age > boomer_age and np.random.rand() < boomer_factor:
        if np.random.randint(2) == 1: suffix = str(birth_year)[-2:] # 50% to remove first two digits from birth year
        mail_domain = np.random.choice(other_domains, p=[0.30, 0.23, 0.23, 0.23, 0.01])

    # Remove century from birth year if age < 60
    elif age < boomer_age:
        if np.random.choice([0,1], p=[0.1, century_removal_p]) == 1: suffix = str(birth_year)[-2:]

    # 50% to remove entire birth year, 25% to add a random int instead
    if force_formal: add_birth_p = [1, 0, 0]
    suffix_modifier = np.random.choice([0,1,3], p=add_birth_p)

    if suffix_modifier == 0: suffix = ''
    elif suffix_modifier == 1: suffix = np.random.randint(1,9)
    else: suffix = str(birth_year)[-2:]

    # 50% to have a first name "nickname", then 20% to only have first letter and .
    if np.random.choice([0, 1], p=[1-nickname_p, nickname_p]) == 1:
        try:
            first, last = name.split()[0], name.split()[1]

            # If length > 7, only use first 3 letters
            if len(first) > 7:
                first = first[:3]
            # if length > 6 only use first 4 letters 
            elif len(first) > 6:
                first = first[:4]

            # 20% to have only the first letter in the first name
            if np.random.choice([0, 1], p=[0.8, 0.2]) == 1:
                first = first[:1] + np.random.choice(['_', '.'])

            name = first + last

        except IndexError:
            # No whitespaces in input string
            print("Name does not contain a space.")


    # Replace blank space and make lowercase
    x = np.random.choice(['_','__','-','.',''],p=[0.1,0.1,0.2,0.1,0.5])
    name = name.lower().replace(' ',x )

    # 10% to add other characters to email
    if np.random.choice([0,1], p=[0.9, 0.1]) == 1:
      prefix = '_'
    else:
      prefix = ''
    

    ################### Replace name entirely #####################


    # millenial_mail_p: float = 0.05,
    # anonymize_mail_p: float = 0.005,
    # apple_hidden_p: float = 0.01,
    # asdf_mail_p: float = 0.05

    # Millenial email if millenial OR millenial p == 1
    if birth_year in range(1989,1998) and np.random.rand() < millenial_mail_p or millenial_mail_p == 1:
        return millenial_mail(birth_year)

    # Completely random and anonymous email
    if np.random.choice([0,1], p=[0.995, 0.005]) == 1 or anonymize == True:
        return anonymize_mail1(is_apple=False) + '@' + mail_domain

    # 1% to have an email hidden by apple services
    if np.random.choice([0,1], p=[0.99, 0.01]) == 1:
      return anonymize_mail1(is_apple=True)

    # 0.5% to have an "asdf" (when users just type "randomly") email:
    if np.random.choice([0,1], p=[0.995, 0.005]) == 1:
      return asdf_mail() + '@' + mail_domain

    ################################################################
        
    return str(prefix) + str(name)+ str(suffix) + '@' + mail_domain


## --- Misc stuff for mail & Anomymize --- ##

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
    word_list1 = ['star', 'cool', 'dark', 'moon', 'knight', 'hunter', '420']
    word_list2 = ['boy', 'girl', 'dude', 'killer', 'fire', 'master']
    separator = ['_', '', '', '-']
    domain_mil = '@' + np.random.choice(['gmail.com','live.com','live.se'])	
    stupid_mail = str(deco) + word_list1[np.random.randint(len(word_list1))] + separator[np.random.randint(len(separator))] + word_list2[np.random.randint(len(word_list2))] + str(deco[::-1])
    if stupid_mail[-1::] == 'x':
        return stupid_mail + domain_mil
    return stupid_mail + str(birth_year)[-2:] + domain_mil


if __name__ == "__main__":
  # print(millenial_mail(1992))
  print(gen_email())
  print(gen_email(age=30, millenial_mail_p=1))