def find_original_set(*args):
    assert len(args) == 10, 'The function expects exactly 10 arguments'
    original_set = set.union(*args)
    for arg in args:
        assert isinstance(arg, set), 'Each argument must be a set'
        assert len(arg) <= 10, 'Each argument must contain at most 10 elements'
        assert len(arg.difference(original_set)) == 0, 'Each argument must be a subset of the original set'
    return original_set