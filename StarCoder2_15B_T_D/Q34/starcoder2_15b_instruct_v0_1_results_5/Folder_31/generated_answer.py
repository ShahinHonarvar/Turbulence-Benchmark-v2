def find_original_set(*args):
    assert len(args) == 34, 'The function must take exactly 34 distinct arguments'
    for arg in args:
        assert isinstance(arg, set), 'Each argument must be a set'
    smallest_set = set.union(*args)
    return smallest_set