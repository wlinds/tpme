import pandas as pd
from utils.utils import generate_datetime

def custom_pre_process():
    market = pd.read_csv("Data/datasets/tamimimarkets.csv")
    general = pd.read_csv("Data/datasets/Ronash_DS_Assignment.csv")

    market['Category'] = 'Food, Beverages & Tobacco'
    market['tags'] = "['snacks']"
    market = market.drop('Size', axis=1)
    market = market.rename(columns={'Prices': 'Price', 'Company': 'Vendor', 'Unnamed: 0': 'product_id'})

    general['Price'] = get_price()
    general['Currency'] = 'SEK'
    general = general.rename(columns={'title': 'Product'})
    general = general.rename(columns={'vendor': 'Vendor', 'category': 'Category'})
    general = general[['product_id', 'Vendor', 'Product', 'Currency', 'Price', 'Category', 'tags']]

    merged_df = pd.concat([general, market], ignore_index=True)

    return merged_df


def get_price():
    # Placeholder # TODO maybe scrape amazon or just randomize?
    return 200.00


import pandas as pd

def generate_expense(keyword=None, category=None, search_by='tags', exclude_word=None):
    df = custom_pre_process()

    if category:
        df = df[df['Category'] == category]

    if keyword:
        if search_by == 'tags':
            df = df[df['tags'].str.contains(keyword, case=False, na=False)]
        elif search_by == 'title':
            df = df[df['Product'].str.contains(keyword, case=False, na=False)]

    if exclude_word:
        if isinstance(exclude_word, str):
            exclude_word = [exclude_word]  # Convert string to list

        for word in exclude_word:
            if search_by == 'tags':
                df = df[~df['tags'].str.contains(word, case=False, na=False)]
            elif search_by == 'title':
                df = df[~df['Product'].str.contains(word, case=False, na=False)]

    if df.empty:
        return None

    selected_row = df.sample(1, random_state=None)

    expense_details = {
        'Category': selected_row['Category'].values[0],
        'Product': selected_row['Product'].values[0],
        'Price': selected_row['Price'].values[0],
        'Currency': selected_row['Currency'].values[0],
        'Datetime': generate_datetime(deviation_p=0)
    }

    return expense_details


if __name__ == "__main__":
    print(generate_expense(keyword="laptop", search_by='title', exclude_word=['backpack', 'bag', 'transport']))