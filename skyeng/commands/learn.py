from argparse import ArgumentParser
from random import shuffle, choice
import subprocess
import re

import huepy
from vlc import MediaPlayer


REX = re.compile(r'(.*)\[(.+)\](.*)')


parser = ArgumentParser('learn')
parser.add_argument('--wordset', required=True, type=int, help='wordset ID')
parser.add_argument('--known', action='store_true', help='Show known words')

parser.add_argument('--repeats', type=int, default=3, help='times of repeats for word')
parser.add_argument('--chunks', type=int, default=3, help='count of chunks of words in learn-write tasks')


def play(url):
    MediaPlayer('https:' + url).play()


def inspect_word(word, repeats=3):
    for _ in range(repeats):
        play(word.info.soundUrl)
        print('{} [{}]'.format(word, word.info.transcription))
        input()

    play(word.info.definition['soundUrl'])
    print(word.info.definition['text'])
    input()

    for example in word.info.examples:
        play(example['soundUrl'])
        print(example['text'])
        input()


def get_chunks(words, n):
    for i in range(0, len(words), n):
        yield words[i:i + n]


def substitute_word(word, text, sound):
    print(REX.sub(r'\1[...]\3', text))
    guess = input('> ')
    if guess.lower() == REX.search(text).groups()[1].lower():
        print(huepy.good("it's right!"))
    elif guess.lower() == word.info.text.lower():
        print(huepy.info("right word, wrong form"))
    else:
        # https://youtu.be/oFlUCr42qzI
        print(huepy.bad("wrong!"))
    play(sound)
    print(text)
    input()


def learn(user, args):
    args = parser.parse_args(args)
    wordset = user.get_wordset(args.wordset)
    words = [word for word in wordset.get_words() if word.is_known is args.known]
    shuffle(words)
    for chunk in get_chunks(words, n=args.chunks):
        for word in chunk:
            inspect_word(word, repeats=args.repeats)
        subprocess.call('clear', shell=True)

        examples = []
        for word in chunk:
            example = choice(word.info.examples)
            examples.append((word, example['text'], example['soundUrl']))
        shuffle(examples)
        for word, text, sound in examples:
            substitute_word(word=word, text=text, sound=sound)
    return 0
