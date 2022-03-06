from math import factorial
import requests
import pytest

@pytest.fixture(params=[0,1,399,699,999])
def numbers(request: int) -> int:
    return request.param

@pytest.fixture()
def method_post_factorial(numbers):
    url = str('http://qainterview.pythonanywhere.com/')
    try:
        response = requests.post(url, data = {'number': numbers})
        data = response.json()
        return data['answer']
    except:
        return response.status_code

@pytest.fixture()
def generate_data_factorial(numbers: int) -> int:
    return factorial(numbers)

