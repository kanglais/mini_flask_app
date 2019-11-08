import requests

def get_response():
    try:
        return requests.get('http://jsonvat.com')
    except:
        return

def check_code_list(response):
    codes = []
    for country in response.json()['rates']:
        codes.append(country['code'])
    return codes


def get_country(country_code, response):
    country_code = country_code.upper()
    for line in response.json()['rates']:
        if line['country_code'] == country_code:
            return line

def get_standard_rate(country):
    for d in country['periods']:
        rates = d['rates']
    return rates['standard']
