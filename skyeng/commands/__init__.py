from .review import review
from .words import words
from .wordsets import wordsets


__all__ = [
    'COMMANDS',
    'review',
    'words',
    'wordsets',
]


COMMANDS = dict(
    review=review,
    words=words,
    wordsets=wordsets,
)
