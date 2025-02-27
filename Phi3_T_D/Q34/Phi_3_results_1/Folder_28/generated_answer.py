from itertools import chain

def find_original_set(*args):
    original_set = set(chain.from_iterable(args))
    return original_set