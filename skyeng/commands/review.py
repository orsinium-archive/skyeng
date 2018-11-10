from argparse import ArgumentParser


PROMT_HELP = """
n - next word
k - I know this word
d - show definition
t - show translation
h - help me!
q - exit
"""


parser = ArgumentParser('review')
parser.add_argument('--wordset', required=True, type=int, help='wordset ID')
parser.add_argument('--known', action='store_true', help='Show known words')


def review(user, args):
    args = parser.parse_args(args)
    wordset = user.get_wordset(args.wordset)
    for word in wordset.get_words():
        if word.is_known is not args.known:
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
            if command == 'q':
                return 0
    return 0
