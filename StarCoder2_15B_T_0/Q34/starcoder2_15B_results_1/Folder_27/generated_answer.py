def find_original_set(*args):
    assert len(args) == 100, 'The function must be passed exactly 100 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Each argument must be a set'
    original_set = set.union(*args)
    return original_set