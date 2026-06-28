import requests
from pprint import pprint

def client():
    token = 'Token abc8de44343871938e76881924383cb9c9291693'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url='http://127.0.0.1:8000/api/kullanici-profilleri/',
        headers = headers,
    )

    print('Status Code : ', response.status_code)
    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()








