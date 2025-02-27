def find_original_set(*args):
    assert len(args) == 18, 'The function must take exactly 18 distinct arguments'
    for arg in args:
        assert isinstance(arg, set), 'Each argument must be a set of integers'
    original_set = set.union(*args)
    return original_set