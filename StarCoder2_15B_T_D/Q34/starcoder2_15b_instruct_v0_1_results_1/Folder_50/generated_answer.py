def find_original_set(*args):
    assert len(args) == 99, 'The function must take exactly 99 distinct arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Each argument must be a set of integers'
    smallest_set = set.union(*args)
    return smallest_set