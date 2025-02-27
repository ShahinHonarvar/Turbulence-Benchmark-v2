def find_original_set(*args):
    assert len(args) == 24, 'Expected exactly 24 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Expected each argument to be a set'
    original_set = set.union(*args)
    return original_set