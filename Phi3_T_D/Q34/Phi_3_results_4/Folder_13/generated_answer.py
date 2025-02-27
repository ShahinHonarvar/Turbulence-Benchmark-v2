from itertools import chain

def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Exactly 845 sets are required as arguments.')
    union_set = set().union(*args)
    return union_set