import pandas as pd

from mapping import TranslationMap
from utils.utils import generate_datetime, hash_string

from features import *
from exporting import export_manager

# GDPR notice: this program can potentially generate real personal data
# Make sure anonymize is TRUE or manually check all generated rows before making anything public

anonymize = False

# Adjust ammount of people / entries to generate
rows = 1000

# Export settings
export_csv = True
export_excel = False
export_sql = False

export_path = 'Exports'
file_name ='tpme_export'

class PersonGenerator:
    def __init__(self, anonymize=True):
        self.anonymize = anonymize
        
    def generate_person(self, 
    
        dist_gender = {'female': 0.5, 'male': 0.5, 'nb': 0.02},
        dist_age = {'mean': 42, 'std': 20, 'lower_lim': 15, 'upper_lim': 100},
        dist_health = {'mean': 3, 'std': 1, 'skewness': 0},
        name_length = {'min_len': 10, 'max_len': 12}

        ):

        age = gen_age(**dist_age)
        phone = gen_phone(anonymize=self.anonymize)
        gendr = gen_gender(self.anonymize, **dist_gender)
        civil = gen_marital(age)
        utbil = gen_education(age)
        syssl = gen_occupation(age)
        boend = gen_accommodation()
        bormd = gen_living_with(age, civil)
        vardt = gen_everyday_satisfaction()
        hälsa = gen_health(**dist_health)

        customer_id = gen_customerID()

        address = gen_address()
        postal = gen_postal()
        city = gen_city()
        country = gen_country()

        # TODO: Finisish tokenization
        name = gen_name(self.anonymize, gendr, **name_length)

        mail = gen_email(name, age, self.anonymize)
        _psw = gen_psw(name, age, self.anonymize)

        # TODO fix this clusterfuck also rename to english
        return (age,name,mail,_psw,phone,gendr,civil,utbil,syssl,boend,bormd,vardt,hälsa, customer_id, address, postal, city, country)

    def customer_generation(self, 
    
        dist_gender = {'female': 0.5, 'male': 0.5, 'nb': 0.02},
        dist_age = {'mean': 42, 'std': 20, 'lower_lim': 15, 'upper_lim': 100},
        name_length = {'min_len': 10, 'max_len': 12}

        ):
        gendr = gen_gender(**dist_gender)
        age = gen_age(**dist_age)
        phone = gen_phone(anonymize=True)
        customer_id = gen_customerID()
        address = gen_address()
        postal = gen_postal()
        city = gen_city()
        country = gen_country()
        name = gen_name(gendr, **name_length)
        mail = _email.gen_email(name, age, anonymize=True)
        _psw = _email.gen_psw(name, age, self.anonymize)

        return (customer_id,name,mail,_psw,phone,address,postal,city,country)


def value_mapper(person_list, language='english', anonymize=False):
    tm = TranslationMap(language=language)

    if isinstance(person_list, tuple):
        person_list = [person_list]

    # Note: Cannot pass a df when using from_records
    df = pd.DataFrame.from_records(person_list, columns=tm.column_names)

    df['Gender'] = df.apply(lambda row: tm.get_translation('Gender', row['Gender']), axis=1)
    df['Marital Status'] = df.apply(lambda row: tm.get_translation('Marital Status', row['Marital Status']), axis=1)
    df['Education'] = df.apply(lambda row: tm.get_translation('Education', row['Education']), axis=1)
    df['Occupation'] = df.apply(lambda row: tm.get_translation('Occupation', row['Occupation']), axis=1)
    df['Accommodation'] = df.apply(lambda row: tm.get_translation('Accommodation', row['Accommodation']), axis=1)
    df['Living with'] = df.apply(lambda row: tm.get_translation('Living with', row['Living with']), axis=1)

    if anonymize:
        print('Hashing selected columns')
        df['Name'] = df['Name'].apply(hash_string, end=8)

    if language == 'swedish':
        df.columns = tm.column_names_swe

    return df


if __name__ == '__main__':

    # Create instance of person class
    pg = PersonGenerator(anonymize=anonymize)
    person_list = [pg.generate_person() for n in range(rows)]

    df = value_mapper(person_list)
    print(df)