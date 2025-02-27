from itertools import chain

def find_original_set(*args):
    return set(chain.from_iterable(args))