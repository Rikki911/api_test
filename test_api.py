import requests
import pytest


@pytest.fixture()
def obj_id():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 20121,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
   yield responce['id']
   requests.delete(f'https://api.restful-api.dev/objects/{responce["id"]}')

def test_create_object():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 20121,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   responce = requests.post('https://api.restful-api.dev/objects', json=payload).json()
   assert responce['name'] == payload['name']


def test_get_object(obj_id):
   print(obj_id)
   response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
   assert response['id'] == obj_id

def test_update_object(obj_id):
   payload = {
         "name": "Apple MacBook Pro 20",
         "data": {
            "year": 20121,
            "price": 1849.99,
            "CPU model": "Intel Core M10",
            "Hard disk size": "1 TB"
         }
      }
   responce = requests.put(
      f'https://api.restful-api.dev/objects/{obj_id}',
      json=payload
   ).json()
   assert responce['name'] == payload['name']

def test_delete_object(obj_id):
   responce = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
   assert responce.status_code == 200
   responce = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
   assert responce.status_code == 404


ff808181932badb601959f908bc25d40
