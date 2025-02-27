def find_original_set(*args):
    assert len(args) == 100, 'The function must be given exactly 100 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Each argument must be a set'
    assert all((len(arg) > 0 for arg in args)), 'Each argument must be a non-empty set'
    original_set = set.union(*args)
    return original_set