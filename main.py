import pandas as pd

from mapping import TranslationMap
from utils.utils import generate_datetime, hash_string

from features import *
from features.tokenized_names import gen_tokenized_name
from exporting import export_manager

VERSION = 'alpha_0.2.2'
anonymize = False

# GDPR notice: this program can potentially generate real personal data
# Make sure anonymize is TRUE or manually check all generated rows before making anything public


# Export settings
export_csv = True
export_excel = False
export_sql = False
export_path = 'Exports'
file_name ='tpme_export'

class PersonGenerator:
    def __init__(self, anonymize=True, name_tokenizer="Experimental"):
        self.anonymize = anonymize
        self.name_tokenizer = name_tokenizer
        
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
        educ = gen_education(age)
        ocup = gen_occupation(age)
        livin = gen_accommodation()
        lwith = gen_living_with(age, civil)
        satis = gen_everyday_satisfaction()
        health = gen_health(**dist_health)

        customer_id = gen_customerID()

        address = gen_address()
        postal = gen_postal()
        city = gen_city()
        country = gen_country()

        if self.name_tokenizer == "Experimental":
            name = gen_tokenized_name(self.anonymize, gendr, **name_length)
        else:
            name = gen_name(self.anonymize, gendr, **name_length)
        mail = gen_email(name, age, self.anonymize)
        _psw = gen_psw(name, age, self.anonymize)

        # TODO fix this clusterfuck
        return (age,name,mail,_psw,phone,gendr,civil,educ,ocup,livin,lwith,satis,health, customer_id, address, postal, city, country)


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
    rows = 10

    # Create instance of person class
    pg = PersonGenerator(anonymize=False, name_tokenizer="Experimental")
    person_list = [pg.generate_person() for n in range(rows)]

    df = value_mapper(person_list)
    print(df)