def find_original_set(*args):
    assert len(args) == 42, 'The function must receive exactly 42 distinct arguments'
    for arg in args:
        assert isinstance(arg, set), 'Each argument must be a set of integers'
    original_set = set.union(*args)
    return original_set