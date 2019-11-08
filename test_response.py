import pytest

from get_json_response import get_response

rates = get_response().json()['rates']

def test_response():
    assert rates
