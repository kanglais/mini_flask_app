import requests

response = requests.get('http://jsonvat.com')

def check_code_list():
    codes = []
    for country in response.json()['rates']:
        codes.append(country['code'])
    return codes


def get_country(country_code):
    for line in response.json()['rates']:
        if line['country_code'] == country_code.upper():
            return line

def get_standard_rate(country):
    for d in country['periods']:
        rates = d['rates']
    return rates['standard']
