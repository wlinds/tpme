
import sys, os, pickle, random
from collections import Counter
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tokenizer import tokenize_names


def gen_tokenized_name(anonymize=True, gender=None, min_len=8, max_len=20, corpus='Data/name_corpus.pkl'):
    if anonymize:
        return "REDACTED"

    try:
        with open(corpus, 'rb') as f:
            name_corpus = pickle.load(f)
    except FileNotFoundError:
        return "nullis corpus"

    if gender == 1:
        first_bucket = [name_corpus['f_norwa_list'], name_corpus['f_scandi_gpt'], name_corpus['f_slavic_gpt'], name_corpus['f_sweden_gpt']]
    elif gender == 2:
        first_bucket = [name_corpus['m_scandi_gpt'], name_corpus['m_slavic_gpt'], name_corpus['m_sweden_gpt']]
    else:
        first_bucket = [
            name_corpus['f_norwa_list'], name_corpus['f_scandi_gpt'], name_corpus['f_slavic_gpt'], name_corpus['f_sweden_gpt'],
            name_corpus['m_scandi_gpt'], name_corpus['m_slavic_gpt'], name_corpus['m_sweden_gpt']
        ]

    last_bucket = [name_corpus['last_gpt_asia'], name_corpus['last_gpt_eur0'], name_corpus['last_gpt_eur2'], name_corpus['last_gpt_mena'], name_corpus['last_swe']]

    first_corpus = [name for sublist in first_bucket for name in sublist]
    last_corpus = [name for sublist in last_bucket for name in sublist]

    first_tokens = tokenize_names(first_corpus)
    last_tokens = tokenize_names(last_corpus)

    first_name = random_name_from_tokens(first_tokens)
    last_name = random_name_from_tokens(last_tokens)

    while len(first_name + last_name) > max_len or len(first_name + last_name) < min_len:
        first_name = random_name_from_tokens(first_tokens)
        last_name = random_name_from_tokens(last_tokens)

    return first_name.capitalize() + ' ' + last_name.capitalize()

def random_name_from_tokens(tokens):
    sorted_tokens = sorted(tokens.keys(), key=lambda x: tokens[x])
    selected_token = np.random.choice(sorted_tokens)
    return selected_token


if __name__ == "__main__":
    print(gen_tokenized_name('Data/name_corpus.pkl', anonymize=False, gender=1))
