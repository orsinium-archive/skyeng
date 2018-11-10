from .learn import learn
from .review import review
from .words import words
from .wordsets import wordsets


__all__ = [
    'COMMANDS',
    'learn',
    'review',
    'words',
    'wordsets',
]


COMMANDS = dict(
    learn=learn,
    review=review,
    words=words,
    wordsets=wordsets,
)
