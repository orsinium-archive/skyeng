import requests
import toml


config = toml.load('./config.toml')
session = requests.session()

session.get('https://id.skyeng.ru/login')
response = session.post(
    'https://id.skyeng.ru/login',
    data=dict(
        _username=config['credentials']['email'],
        _password=config['credentials']['password'],
    ),
)

response = session.post('https://rooms.vimbox.skyeng.ru/users/api/v1/auth/auth')
token = response.json()['token']

response = session.get(
    'https://api.words.skyeng.ru/api/v1/userInfo.json',
    headers=dict(Authorization='Bearer ' + token),
)

user_id = response.json()['profile']['userId']

response = session.get(
    'https://api.words.skyeng.ru/api/for-vimbox/v1/wordsets.json',
    params=dict(studentId=user_id, pageSize=100, page=1),
    headers=dict(Authorization='Bearer ' + token),
)

courses = dict()
for course in response.json()['data']:
    courses[course['id']] = course['title']


response = session.get(
    'https://api.words.skyeng.ru/api/for-training/v1/wordsets/{}/words.json'.format(11434584),
    params=dict(studentId=user_id, pageSize=100, page=1),
    headers=dict(Authorization='Bearer ' + token),
)
words_ids = [word['meaningId'] for word in response.json()['data']]


response = session.get(
    'https://dictionary.skyeng.ru/api/for-mobile/v1/meanings',
    params=dict(ids=','.join(map(str, words_ids))),
    headers=dict(Authorization='Bearer ' + token),
)
words = response.json()
# text, transcription, translation/text, isGold3000, examples, soundUrl

# GET https://api.words.skyeng.ru/api/v1/userWords.json?userId=1903783&meaningIds=218484,19506...
# GET https://dictionary.skyeng.ru/api/public/v1/words/search?search=brain
