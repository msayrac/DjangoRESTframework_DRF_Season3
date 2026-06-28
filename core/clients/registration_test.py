import requests
from pprint import pprint

def client():
    credentials = {
        'username':'testuserrest3',
        'email':'testuserrest@gmail.com',
        'password1':'Admin1234.',
        'password2':'Admin1234.'

    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/', #/api/rest-auth/registration/
        data=credentials,
    )

    print('Status Code : ', response.status_code)
    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()










