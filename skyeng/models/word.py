from datetime import datetime, timezone
from .base import Base


class Word(Base):
    @property
    def definition(self):
        return '{word} [{transcription}] — {description}'.format(
            word=self.info.text,
            transcription=self.info.transcription,
            description=self.info.definition['text'],
        )

    def update(self, status=None, answers=None, interval=None):
        if status is None:
            # in progress, known...
            status = self.info.status
        if answers is None:
            answers = self.info.correctAnswersNumber
        if interval is None:
            interval = self.info.trainingIntervalsNumber

        now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        request = dict(
            currentDateTime=now,
            words=[dict(
                id=self.info.id,
                meaningId=self.info.meaningId,

                correctAnswersNumber=answers,
                status=status,
                trainingIntervalsNumber=interval,

                trainedAt=now,
                updatedAt=now,
            )],
        )
        response = self.session.post(
            'https://api.words.skyeng.ru/api/v1/words/synchronize.json',
            json=request,
        )
        return response.status_code == 204

    @property
    def is_known(self):
        return self.info.status == 'known'

    def __str__(self):
        return self.info.text
