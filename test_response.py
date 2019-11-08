import pytest

import get_json_response

def test_response():
    country_code = 'NL'
    response = get_json_response.get_response()
    country = get_json_response.get_country(country_code, response)
    assert country['name'] == 'Netherlands'