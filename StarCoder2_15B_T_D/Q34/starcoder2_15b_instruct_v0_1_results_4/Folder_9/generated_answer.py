def find_original_set(*args):
    assert len(args) == 73, 'The function must take exactly 73 distinct arguments'
    original_set = set.union(*args)
    return original_set