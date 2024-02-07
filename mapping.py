
class TranslationMap:
    def __init__(self, language='english'):
        self.language = language.lower()
        
        self.translation_maps = {
            'english': {
                'Gender': {1: 'Female', 2: 'Male', 3: 'Other'},
                'Marital Status': {1: 'Married/Common-law partner', 2: 'Widow/Widower not remarried', 3: 'Divorced, not remarried', 4: 'Living separately but not divorced', 5: 'Single', 6: 'Other'},
                'Education': {1: 'Elementary school level or lower', 2: 'Primary school/Secondary school', 3: 'High school diploma', 4: 'Folk high school/Vocational education', 5: 'Incomplete academic education', 6: 'University/College degree'},
                'Occupation': {1: 'Employed', 2: 'Student', 3: 'Unemployed', 4: 'On sick leave/disability pension', 5: 'Retired', 6: 'Not employed for other reasons'},
                'Accommodation': {1: 'Rental apartment', 2: 'Condominium', 3: 'Townhouse, cottage, or similar', 4: 'Special housing', 5: 'Other'},
                'Living with': {1: 'Living alone', 2: 'Spouse/partner', 3: 'Children', 4: 'Parent', 5: 'Other', 6: 'Family (Partner and children/parents and siblings)'}
            },
            'swedish': {
                'Gender': {1: 'Kvinna', 2: 'Man', 3: 'Annat'},
                'Marital Status': {1: 'Gift/Sambo', 2: 'Änka/Änkling ej omgift', 3: 'Skild, ej omgift', 4: 'Särbo', 5: 'Ogift', 6: 'Annat'},
                'Education': {1: 'Folkskolenivå eller lägre', 2: 'Grundskola/Realexamen', 3: 'Studentexamen', 4: 'Fölkhögskola/Yrkesutbildning', 5: 'Ofullständig akademisk utbildning', 6: 'Universitet/Högskola med examen'},
                'Occupation': {1: 'Arbete', 2: 'Studier', 3: 'Arbetslös', 4: 'Sjukskriven/sjukersättning', 5: 'Ålderspensionär', 6: 'Icke-förvärvsarbetande av annan orsak'},
                'Accommodation': {1: 'Hyresrätt', 2: 'Bostadrätt', 3: 'Radhus, villa eller liknande', 4: 'Särskilt boende', 5: 'Annat'},
                'Living with': {1: 'Ensamboende', 2: 'Make/maka/sambo', 3: 'Barn', 4: 'Förälder', 5: 'Annan', 6: 'Familj (Partner och barn/ föräldrar och syskon)'}
            }
        }

        self.column_names = ['Age', 'Name', 'Email', 'Password', 'Phone', 'Gender', 'Marital Status',
                                            'Education', 'Occupation', 'Accommodation', 'Living with',
                                            'Everyday satisfaction', 'Health']

        self.column_names_swe = ['Ålder','Namn', 'Email', 'Lösenord', 'Telefon', 'Kön', 'Civilstånd', 'Utbildningsnivå', 'Sysselsättning', 'Boende', 'Tillsammans_med', 'Vardagstillfredsställelse', 'Hälsa']

    def get_translation(self, column, key):
        if self.language in self.translation_maps and column in self.translation_maps[self.language] and key in self.translation_maps[self.language][column]:
            return self.translation_maps[self.language][column][key]
        return f'Not found: {key} in column {column}'