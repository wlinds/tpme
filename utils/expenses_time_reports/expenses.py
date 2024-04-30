import pandas as pd
from utils.utils import generate_datetime
import numpy as np

def default_dataset():
    market = pd.read_csv("Data/datasets/tamimimarkets.csv")
    general = pd.read_csv("Data/datasets/Ronash_DS_Assignment.csv")
    dog_treats = pd.read_csv("Data/datasets/dog_treats.csv")

    dog_treats['Category'] = 'Animals & Pet Supplies'
 
    market['Category'] = 'Food, Beverages & Tobacco'
    market['tags'] = "['snacks']"
    market = market.drop('Size', axis=1)
    market = market.rename(columns={'Prices': 'Price', 'Company': 'Vendor', 'Unnamed: 0': 'product_id'})

    general['Price'] = get_price()
    general['Currency'] = 'SEK'
    general = general.rename(columns={'title': 'Product'})
    general = general.rename(columns={'vendor': 'Vendor', 'category': 'Category'})
    general = general[['product_id', 'Vendor', 'Product', 'Currency', 'Price', 'Category', 'tags']]

    merged_df = pd.concat([general, market, dog_treats], ignore_index=True)

    merged_df = merged_df.drop(['tags', 'Size'], axis=1)

    return merged_df

def get_dataset(dataset='default', category=None, custom_path=None):
    if custom_path:
        print(f'Loading dataset from path {custom_path}')
        try:
            df = pd.read_csv(custom_path)
            print(f'Created {df.columns}')
            return df
        except Exception as e:
            print(f'Error loading dataset: {e}')
            return None

    
    if dataset=='default':
        df = default_dataset()

    if category:
        df = df[df['Category'] == category]

    

    return df


def get_price():
    # Placeholder # TODO maybe scrape amazon or just randomize?
    return 200.00


def generate_expense(keyword=None, category=None, search_by='tags', exclude_word=None, date_time=False, custom_path=None):

    df = get_dataset(dataset='default', category=category, custom_path=custom_path)

    if category and not custom_path:
        df = df[df['Category'] == category]

    if keyword and not custom_path:
        if search_by == 'tags':
            df = df[df['tags'].str.contains(keyword, case=False, na=False)]
        elif search_by == 'title':
            df = df[df['Product'].str.contains(keyword, case=False, na=False)]

    if exclude_word:
        if isinstance(exclude_word, str):
            exclude_word = [exclude_word]

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
        'Vendor': selected_row['Vendor'].values[0],
        'Product': selected_row['Product'].values[0],
        # 'product_id': selected_row['product_id'].values[0],
        'ArticleNr': selected_row['ID'].values[0],
        'Price': selected_row['Price'].values[0],
        # 'Currency': selected_row['Currency'].values[0]
    }

    if date_time:
        expense_details['Datetime'] = generate_datetime(deviation_p=0)

    return expense_details


def generate_orders(df, n_orders, start_at=None, category=None):

    print(df['Customer ID'])

    customer_ids = df['Customer ID'].unique()

    order_ids = []
    customer_id_list = []
    order_dates = []
    order_statuses = []

    current_order_id = 0

    for customer_id in customer_ids:
        order_date = generate_datetime()

        for _ in range(n_orders):
            if start_at is None:
                # Generate random order ID
                order_id = np.random.randint(100000, 999999)
            else:
                # Generate sequential order ID starting at start_at
                order_id = start_at + current_order_id
                current_order_id += 1

            order_ids.append(order_id)
            customer_id_list.append(customer_id)
            order_dates.append(order_date)
            order_statuses.append(np.random.choice(['Pending', 'Processing', 'Shipped', 'Delivered']))


    orders_df = pd.DataFrame({
        'Customer ID': customer_id_list,
        'Order ID': order_ids,
        'Order Date': order_dates,
        'Order Status': order_statuses
    })

    orders_df['Order Status'] = np.random.choice(['Pending', 'Processing', 'Shipped', 'Delivered'], size=len(orders_df))

    #orders_details = generate_order_details(orders_df)


    return orders_df, #orders_details



def generate_order_details(orders_df, custom_path=None, min_n_orders=1, max_n_orders=1):
    # df = df.drop(['Order Date', 'Customer ID', 'Order Status'], axis=1)
    df = orders_df.drop(['datetime', 'Status', 'CustomerID'], axis=1)

    vendors = []
    products = []
    prices = []
    currencies = []
    units = []
    order_ids = []  # Keep track of Order ID for each row
    product_ids = []

    for _, row in df.iterrows():
        if min_n_orders == max_n_orders:
            expense_count = max_n_orders
        else:
            expense_count = np.random.randint(min_n_orders, max_n_orders)

        for _ in range(expense_count):
            expense_details = generate_expense(category="Animals & Pet Supplies", custom_path=custom_path)

            # product_ids.append(expense_details['product_id'])
            product_ids.append(expense_details['ArticleNr'])

            vendors.append(expense_details['Vendor'])
            products.append(expense_details['Product'])
            prices.append(expense_details['Price'])
            # currencies.append(expense_details['Currency'])
            units.append(np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], p=[0.5, 0.05, 0.05, 0.1, 0.025, 0.1, 0.025, 0.025, 0.025, 0.1]))
            # order_ids.append(row['Order ID'])
            order_ids.append(row['ID'])

    print(len(vendors))
    print(len(products))
    print(len(prices))
    print(len(currencies))
    print(len(units))
    print(len(order_ids))
    print(len(product_ids))

    # Create a new DataFrame with the generated data
    orders_details_df = pd.DataFrame({
        'Order ID': order_ids,
        # 'Vendor': vendors,
        'ID': product_ids,
        # 'Product': products,
        'Quantity': units,
        'Unit Price': prices,
        # 'Currency': currencies
    })

    return orders_details_df




if __name__ == "__main__":
    print(generate_expense(keyword="Dog Treats", search_by='title', exclude_word=['backpack', 'bag', 'transport'], date_time=False))
    # products = get_dataset()

    # print(products['Category'].unique)

