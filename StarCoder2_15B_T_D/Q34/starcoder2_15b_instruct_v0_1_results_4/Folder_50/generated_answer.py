def find_original_set(*args):
    assert len(args) == 99
    original_set = set.union(*args)
    return original_set