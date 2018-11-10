

def wordsets(user, args):
    wordsets = user.get_wordsets()
    for wordset in wordsets:
        print('{:8}. {} ({}%)'.format(wordset.info.id, wordset, wordset.info.progress))
    return 0
