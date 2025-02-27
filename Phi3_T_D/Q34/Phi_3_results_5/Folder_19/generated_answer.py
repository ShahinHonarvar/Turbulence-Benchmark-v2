def find_original_set(*args):
    if len(args) != 23 or any((len(s) != len(set(s)) for s in args)):
        raise ValueError('Exactly 23 distinct sets of integers are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set