from argparse import ArgumentParser


parser = ArgumentParser('words')
parser.add_argument('--wordset', required=True, type=int, help='wordset ID')
parser.add_argument('--known', action='store_true', help='Show known words')


def words(user, args):
    args = parser.parse_args(args)
    wordset = user.get_wordset(args.wordset)
    for word in wordset.get_words():
        if word.is_known is not args.known:
            continue
        print(word.definition)
    return 0
