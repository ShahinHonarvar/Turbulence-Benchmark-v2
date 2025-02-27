def find_original_set(*args):
    assert len(args) == 87, 'The function must take exactly 87 distinct arguments'
    original_set = set.union(*args)
    for arg in args:
        assert isinstance(arg, set) and all((isinstance(item, int) for item in arg)), 'Each argument must be a set of integers'
    return original_set