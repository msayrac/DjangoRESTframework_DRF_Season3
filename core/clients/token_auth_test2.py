import requests
from pprint import pprint

def client():
    token = 'Token 43bd243dae3f5072d8db527ade1541a746320260'

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








