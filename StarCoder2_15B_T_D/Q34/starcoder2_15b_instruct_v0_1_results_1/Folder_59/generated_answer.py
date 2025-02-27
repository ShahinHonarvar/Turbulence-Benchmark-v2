def find_original_set(*args):
    assert len(args) == 10, 'Expected exactly 10 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Expected each argument to be a set'
    original_set = set.union(*args)
    return original_set