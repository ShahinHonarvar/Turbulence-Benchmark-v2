def find_original_set(*args):
    if len(args) != 51 or any((len(set(arg)) != len(arg) for arg in args)):
        raise ValueError('Exactly 51 distinct sets of integers are required.')
    result = frozenset().union(*args)
    return result