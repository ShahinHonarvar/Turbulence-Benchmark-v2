def find_original_set(*args):
    assert len(args) == 19, 'The function must take exactly 19 distinct arguments'
    for arg in args:
        assert type(arg) == set, 'Each argument must be a set of integers'
    original_set = set.union(*args)
    for arg in args:
        assert arg.issubset(original_set), 'Each argument must be a subset of the original set'
    return original_set