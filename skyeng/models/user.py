from .base import Base
from .wordset import WordSet


class User(Base):
    def get_wordsets(self):
        response = self.session.get(
            'https://api.words.skyeng.ru/api/for-vimbox/v1/wordsets.json',
            params=dict(studentId=self.info.id, pageSize=100, page=1),
        )
        return [
            WordSet(session=self.session, info=info, user=self)
            for info in response.json()['data']
        ]

    def get_wordset(self, wordset_id):
        for wordset in self.get_wordsets():
            if wordset.info.id == wordset_id:
                return wordset
        raise KeyError('WordSet with given ID not found')

    def __str__(self):
        return self.info.email
