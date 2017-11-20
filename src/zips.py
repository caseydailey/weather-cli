import pandas

zip_list = list(pandas.read_csv('../assets/us_postal_codes.csv')['Zip Code'])

def get_zips():
    return zip_list