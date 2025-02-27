def find_original_set(*args):
    assert len(args) == 702, 'Expected 702 distinct arguments'
    original_set = set.union(*args)
    return original_set