#Start in terminal: pytest reqres_test_api.py -s
#Description: Presented HTTP methods for API testing: GET, POST, PUT, PATCH, DELETE
#Site: https://reqres.in

import pytest
import requests

url = str('https://reqres.in')

def test_get_list_users():
    response = requests.get(url + '/api/users?page=2')
    #print(response.content)
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(url + '/api/users/2')
    #print(response.content)
    assert response.status_code == 200

def test_get_single_user_not_found():
    response = requests.get(url + '/api/users/23')
    #print(response.content)
    assert response.status_code == 404

def test_get_list_resource():
    response = requests.get(url + '/api/unknown')
    #print(response.content)
    assert response.status_code == 200

def test_get_single_resource():
    response = requests.get(url + '/api/unknown/2')
    #print(response.content)
    assert response.status_code == 200

def test_get_single_resource_not_found():
    response = requests.get(url + '/api/unknown/23')
    #print(response.content)
    assert response.status_code == 404

def test_post_create():
    response = requests.post(url + '/api/users/', data = {'name':'morpheus', 'job':'leader'})
    #print(response.content)
    assert response.status_code == 201

def test_put_update():
    response = requests.put(url + '/api/users/2', data = {'name':'morpheus', 'job':'zion resident'})
    #print(response.content)
    assert response.status_code == 200

def test_patch_update():
    response = requests.patch(url + '/api/users/2', data = {'name':'morpheus', 'job':'zion resident'})
    #print(response.content)
    assert response.status_code == 200

def test_delete():
    response = requests.delete(url + '/api/users/2')
    #print(response.content)
    assert response.status_code == 204

def test_post_register_successful():
    response = requests.post(url + '/api/register/', data = {'email':'eve.holt@reqres.in', 'password':'pistol'})
    #print(response.content)
    assert response.status_code == 200

def test_post_register_unsuccessful():
    response = requests.post(url + '/api/register/', data = {'email':'sydney@fife'})
    #print(response.content)
    assert response.status_code == 400

def test_post_login_successful():
    response = requests.post(url + '/api/login/', data = {'email':'eve.holt@reqres.in', 'password':'cityslicka'})
    #print(response.content)
    assert response.status_code == 200

def test_post_login_unsuccessful():
    response = requests.post(url + '/api/login/', data = {'email':'peter@klaven'})
    #print(response.content)
    assert response.status_code == 400

def test_get_delayed_response():
    response = requests.get(url + '/api/users?delay=3')
    #print(response.content)
    assert response.status_code == 200
