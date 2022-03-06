from math import factorial
import requests
import sys 

url = str('http://qainterview.pythonanywhere.com/')

def method_post_factorial(number: int) -> int:
    """ The function sends a value to the server
    to calculate the factorial of a number, then
    receives a response, which is then hashed """
    response = requests.post(url, data = {'number': number})
    try:
        data = response.json()
        encode = hash(data['answer'])
        print('Response Server: ', encode)
    except:
        print('Response Server: ', response)

def generate_data_factorial(number: int) -> int:
    """ The function calculates the factorial
    of the input value,then hashes the data """
    try:
        data = int(number)
        encode = hash(factorial(data))
        print('Equal: ', encode)
    except ValueError as e:
        print('Equal Error: ', e)

if __name__ == '__main__':
    try:
        number = int(sys.argv[1])
        method_post_factorial(number)
        generate_data_factorial(number)
    except ValueError as e:
        print('Error: ', e)
    except IndexError as e:
        print('Error: ', e)
