import requests
from .models.user import User


class Session:
    def __init__(self):
        self._session = requests.session()

    def auth(self, email, password):
        self._session.get('https://id.skyeng.ru/login')
        self._session.post(
            'https://id.skyeng.ru/login',
            data=dict(
                _username=email,
                _password=password,
            ),
        )
        response = self._session.post('https://rooms.vimbox.skyeng.ru/users/api/v1/auth/auth')
        self.token = response.json()['token']
        self.headers = dict(Authorization='Bearer ' + self.token)
        return self.token

    def get(self, url, **kwargs):
        return self._session.get(url, headers=self.headers, **kwargs)

    def post(self, url, **kwargs):
        return self._session.post(url, headers=self.headers, **kwargs)

    def get_user(self):
        response = self.get('https://api.words.skyeng.ru/api/v1/userInfo.json')
        data = response.json().copy()
        data.update(data['profile'])
        del data['profile']
        return User(session=self, info=data)
