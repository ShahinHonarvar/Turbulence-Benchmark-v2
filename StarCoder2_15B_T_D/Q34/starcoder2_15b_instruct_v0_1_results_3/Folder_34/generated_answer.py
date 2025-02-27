def find_original_set(*args):
    assert len(args) == 95, 'Expected 95 distinct arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Each argument must be a set'
    original_set = set.union(*args)
    return original_set