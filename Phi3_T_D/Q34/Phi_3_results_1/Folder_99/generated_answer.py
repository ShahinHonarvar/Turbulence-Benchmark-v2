from itertools import chain

def find_original_set(*args):
    if any((len(arg) != len(set(arg)) for arg in args)):
        raise ValueError('All sets must contain distinct integers.')
    if len(args) != 415:
        raise ValueError('Exactly 415 arguments are required.')
    return set(chain.from_iterable(args))