import numpy as np
import pickle


def gen_name(gender=None, min_len=8, max_len=20):
  # awful structure, TODO: optimize. actually no, the entire name generation shoud be rewritten

  try:
      file_path = 'Data/name_corpus.pkl'
      with open(file_path, 'rb') as f:
          name_corpus = pickle.load(f)
          print(name_corpus.keys())

  except FileNotFoundError:
      return "nullis corpus"

  if gender == 1:
      first_bucket = [name_corpus['f_norwa_list'], name_corpus['f_scandi_gpt'], name_corpus['f_slavic_gpt'], name_corpus['f_sweden_gpt']]
  elif gender == 2:  
      first_bucket = [name_corpus['m_scandi_gpt'], name_corpus['m_slavic_gpt'], name_corpus['m_sweden_gpt']]
  elif gender == 3 or gender == None:
      first_bucket = [name_corpus['f_norwa_list'], name_corpus['f_scandi_gpt'], name_corpus['f_slavic_gpt'], name_corpus['f_sweden_gpt'], name_corpus['m_scandi_gpt'], name_corpus['m_slavic_gpt'], name_corpus['m_sweden_gpt']]

  # Here maybe last names should be adjusted to match first names according to cultural status quo
  last_bucket = [name_corpus['last_gpt_asia'], name_corpus['last_gpt_eur0'], name_corpus['last_gpt_eur2'], name_corpus['last_gpt_mena'], name_corpus['last_swe']]

  first_name = random_name_from_bucket(first_bucket)
  last_name = random_name_from_bucket(last_bucket)

  while len(last_name) + len(first_name) > max_len or len(last_name) + len(first_name) < min_len:
      first_name = random_name_from_bucket(first_bucket)
      last_name = random_name_from_bucket(last_bucket)

  return first_name + ' ' + last_name


def random_name_from_bucket(name_bucket):
    selected_name_list = name_bucket[np.random.randint(0, len(name_bucket))]
    selected_name = selected_name_list[np.random.randint(0, len(selected_name_list))]
    return selected_name

if __name__ == "__main__":
    print(gen_name())