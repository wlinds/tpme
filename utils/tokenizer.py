import pickle, random
from collections import Counter
import pandas as pd

def get_corpus(file_path='Data/name_corpus.pkl'):
    try:
        with open(file_path, 'rb') as f:
            name_corpus = pickle.load(f)

        return name_corpus

    except FileNotFoundError:
        return "null corpus"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def extract_lists_and_dicts(corpus, verbose=False):
    if verbose:
        print(f"Found {len(corpus.keys())} keys in corpus: {corpus.keys()}.")

    extracted_words = []

    def recursive_extract(item):
        if isinstance(item, list):
            for i in item:
                recursive_extract(i)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_extract(value)
        else:
            extracted_words.append(item)

    recursive_extract(corpus)

    if verbose:
        print('Done extracting nested dictionaries and lists.')

    return extracted_words

def find_most_common_values(lst, n):
    return Counter(lst).most_common(n)

def get_word(split_word_dict, target_token):
    for key, token in split_word_dict.items():
        if token == target_token:
            return key
    return None

def get_token(split_word_dict, target_key):
    for key, token in split_word_dict.items():
        if key == target_key:
            return token
    return None

def tokenize_names(corpus, start_length=2, split_type='median', apply_rules=None, verbose=False):

    if isinstance(corpus, dict):
        corpus = extract_lists_and_dicts(corpus, verbose)

    split_word_dict = {}
    all_parts = []  # For stats

    if split_type == 'median':
        split_function = median_split
    elif split_type == 'three_way':
        split_function = three_way_split
    else:
        raise ValueError(f"Unknown split_type: {split_type}")

    for word in corpus:
        parts = split_function(word)
        all_parts.extend(parts)

    frequency_counter = Counter(all_parts)

    sorted_tokens = sorted(frequency_counter.keys(), key=lambda x: -frequency_counter[x])

    token_index = 1
    for token in sorted_tokens:
        split_word_dict[token] = token_index
        token_index += 1

    if verbose:
        verbose_print(corpus, all_parts, split_word_dict, split_type, apply_rules)

    return split_word_dict

def median_split(w):
    """Simplest form of splitting word in half"""
    w = w.lower()
    med = len(w) // 2
    return w[:med], w[med:]

def three_way_split(w):
    """Split the word into three parts"""
    w = w.lower()
    length = len(w)
    med1 = length // 3
    med2 = 2 * length // 3
    return w[:med1], w[med1:med2], w[med2:]

def smart_split(w):

    return

def verbose_print(corpus, all_parts, split_word_dict, split_type, apply_rules):
    print(f'\nTokenization running. Found {len(corpus)} words.')
    print(f'{split_type=}')
    print(f'{apply_rules=}\n')

    unique_tokens = len(split_word_dict)
    total_combinations = combinations(unique_tokens, 2)

    print(f'Total tokens : {len(all_parts)}')
    print(f'Unique tokens: {unique_tokens}')
    print(f'Allowed pairs: {total_combinations}\n')

    top_n = 3
    print(f'Top {top_n} tokens:')
    for word, count in find_most_common_values(all_parts, top_n):
        print(f'"{word}", freq: {count}, token: {get_token(split_word_dict, word)}')

    split_word_list = list(split_word_dict)

    print(f'\nExample generations (token pairs):')
    for i in range(3):
        w1 = random.choice(split_word_list)
        w2 = random.choice(split_word_list)

        print(w1.capitalize() + w2, end='')
        print(',', split_word_dict[w1], split_word_dict[w2])


def check_redundacy():
    corpus = get_corpus()
    words = extract_lists_and_dicts(corpus)
    split_word_dict = tokenize(corpus, verbose=False)

    def get_tokens(word):
        word_lower = word.lower()
        tokens = []
        
        for i in range(len(word_lower)):
            for j in range(i + 1, len(word_lower) + 1):
                substring = word_lower[i:j]
                token = split_word_dict.get(substring, None)
                if token is not None:
                    tokens.append(token)
                    
        return tokens

    df = pd.DataFrame({'Name': words})

    df['Tokens'] = df['Name'].apply(get_tokens)

    return df


if __name__ == "__main__":
    # print(median_split("Johan"))
    name_corpus = get_corpus()
    test_bucket = name_corpus['m_sweden_gpt']

    # tokens = tokenize(test_bucket)
    tokens = tokenize(name_corpus)
    print(tokens)


    #check_redundacy()
