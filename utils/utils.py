import random
from datetime import datetime, timedelta, time
import pandas as pd

## Aditional script to generate datetime and expenses

def generate_datetime(date_threshold=None, time_threshold=None, deviation_p=0.01, verbose=True):
    """
    Generate a random datetime object within specified date and time thresholds.

    Parameters:
    - date_threshold (tuple, optional): Tuple of datetime objects or strings representing the start and end dates.
      Defaults to the last 14 days from the current date.
    - time_threshold (tuple, optional): Tuple of time objects or strings representing the start and end times of a day.
      Defaults to 08:00 to 19:30.
    - deviation_p (float, optional): Probability of deviating from the time threshold. Defaults to 0.01.
      A higher value increases the likelihood of deviation.
    - verbose (bool, optional): If True, prints a message when deviation is triggered. Defaults to True.

    Returns:
    str: Randomly generated datetime in the format 'YYYY-MM-DD HH:MM:SS' within the specified thresholds.

    Example:
    >>> generate_datetime()
    '2024-02-11 12:42:42'

    Note:
    - If deviation is triggered, the generated time will be outside the specified time_threshold.
      The deviation information will be printed if verbose is True.

    """
    
    # Handle input & set default values
    if date_threshold is None:
        date_threshold = (datetime.now() - timedelta(days=14), datetime.now())
    elif isinstance(date_threshold[0], str):
        date_threshold = (
            datetime.strptime(date_threshold[0], "%Y-%m-%d"),
            datetime.strptime(date_threshold[1], "%Y-%m-%d")
        )

    if time_threshold is None:
        time_threshold = (time(8, 0), time(19, 30))
    elif isinstance(time_threshold[0], str):
        time_threshold = (
            datetime.strptime(time_threshold[0], "%H:%M:%S").time(),
            datetime.strptime(time_threshold[1], "%H:%M:%S").time()
        )

    start_date, end_date = date_threshold
    random_date = start_date + timedelta(seconds=(end_date - start_date).total_seconds() * random.random())

    if random.random() > deviation_p:
        # Generate time within the threshold
        start_time, end_time = time_threshold
        random_seconds = random.randint(start_time.hour * 3600 + start_time.minute * 60,
                                         end_time.hour * 3600 + end_time.minute * 60)
        random_time = time(random_seconds // 3600, (random_seconds % 3600) // 60, random_seconds % 60)
    else:
        # Generate time outside the threshold (deviation triggered)
        random_time = random_date.time()
        if verbose:
            print(f'Deviation triggered during datetime generation. {deviation_p=}')

    res = random_date.replace(hour=random_time.hour, minute=random_time.minute, second=random_time.second).strftime('%Y-%m-%d %H:%M:%S')

    return res


def get_expenses():
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
    # Placeholder # TODO
    return 200.00


def generate_expenses(keyword=None, category=None):
    df = get_expenses()

    if category:
        df = df[df['Category'] == category]

    if keyword:
        df = df[df['tags'].str.contains(keyword, case=False, na=False)]

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
    print(generate_datetime())
    print(generate_datetime(('2012-01-01','2012-12-12'),('08:00:01','09:01:13')))
    print(generate_expenses())