def find_original_set(*args):
    assert len(args) == 13, 'The function must take exactly 13 distinct arguments'
    original_set = set.union(*args)
    return original_set