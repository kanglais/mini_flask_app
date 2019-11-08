import pytest

from get_json_response import get_response

response = get_response()

def test_response():

    assert str(response) == '<Response [200]>'
