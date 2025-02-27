from itertools import chain

def find_original_set(*sets):
    if len(sets) != 733:
        raise ValueError('Exactly 733 sets required')
    if any((not isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets')
    if any((len(s) != len(s.intersection(*sets)) for s in sets)):
        raise ValueError('Sets must be distinct and intersect with each other')
    union_set = set().union(*sets)
    return union_set