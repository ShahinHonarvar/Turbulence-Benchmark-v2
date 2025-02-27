def find_original_set(*args):
    assert len(args) == 67
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set