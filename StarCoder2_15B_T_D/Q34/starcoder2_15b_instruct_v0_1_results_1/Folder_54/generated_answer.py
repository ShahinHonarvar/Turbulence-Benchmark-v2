def find_original_set(*args):
    assert len(args) == 74, 'The function should take exactly 74 distinct arguments'
    original_set = set.union(*args)
    return original_set