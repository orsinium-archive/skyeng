from argparse import ArgumentParser

import toml

from .session import Session


parser = ArgumentParser(prog='skyeng')
parser.add_argument('-c', '--config', default='./config.toml')
parser.add_argument('--wordsets', action='store_true', help='Show wordsets and exit')
parser.add_argument('--wordset', type=int, help='Show words for given wordset ID and exit')
parser.add_argument('-i', '--interactive', action='store_true', help='Show promt for every word')
parser.add_argument('--known', action='store_true', help='Show known words')


PROMT_HELP = """
n - next word
k - I know this word
d - show definition
t - show translation
h - help me!
q - exit
"""


def cli(args):
    args = parser.parse_args(args)
    config = toml.load(args.config)
    session = Session()
    session.auth(
        email=config['credentials']['email'],
        password=config['credentials']['password'],
    )
    user = session.get_user()

    if args.wordsets:
        wordsets = user.get_wordsets()
        for wordset in wordsets:
            print('{:8}. {} ({}%)'.format(wordset.info.id, wordset, wordset.info.progress))
        return 0

    if args.wordset:
        wordset = user.get_wordset(args.wordset)
        if args.interactive:
            print(PROMT_HELP)
        for word in wordset.get_words():
            if word.is_known != args.known:
                continue

            if not args.interactive:
                print(word.definition)
                continue

            print(word)
            while 1:
                command = input('> ')
                if command == 'n':
                    break
                if command == 'k':
                    if word.update(status='known'):
                        print('OK')
                    else:
                        print('FAIL')
                    break
                if command == 'd':
                    print(word.definition)
                if command == 't':
                    print(word.info.translation['text'])
                if command == 'h':
                    print(PROMT_HELP)
                if command == '1':
                    return 0

        return 0
