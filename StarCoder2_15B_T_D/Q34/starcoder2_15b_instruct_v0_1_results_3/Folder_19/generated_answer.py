def find_original_set(*args):
    assert len(args) == 23, 'The function must take exactly 23 distinct arguments'
    original_set = set.union(*args)
    return original_set