from .base import Base
from .word import Word


class WordSet(Base):
    def __init__(self, session, info, user):
        self.user = user
        super().__init__(session=session, info=info)

    def get_words(self):
        response = self.session.get(
            'https://api.words.skyeng.ru/api/for-training/v1/wordsets/{}/words.json'.format(self.info.id),
            params=dict(studentId=self.user.info.id, pageSize=100, page=1),
        )
        words_info = {int(word['meaningId']): word for word in response.json()['data']}
        words_ids = [word['meaningId'] for word in response.json()['data']]

        response = self.session.get(
            'https://dictionary.skyeng.ru/api/for-mobile/v1/meanings',
            params=dict(ids=','.join(map(str, words_ids))),
        )

        result = []
        for info in response.json():
            info.update(words_info[int(info['id'])])
            result.append(Word(session=self.session, info=info))
        return result

    def __str__(self):
        return self.info.title
