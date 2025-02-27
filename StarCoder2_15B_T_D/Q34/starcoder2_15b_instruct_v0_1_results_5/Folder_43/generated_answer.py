def find_original_set(*args):
    assert len(args) == 49, 'The function must take exactly 49 distinct arguments'
    for arg in args:
        assert isinstance(arg, set) and all((isinstance(x, int) for x in arg)), 'Each argument must be a set of integers'
    original_set = set.union(*args)
    return original_set