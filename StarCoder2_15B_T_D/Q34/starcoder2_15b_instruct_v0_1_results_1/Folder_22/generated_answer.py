def find_original_set(*args):
    assert len(args) == 24, 'Expected exactly 24 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Expected arguments to be sets'
    assert all((len(arg) > 0 for arg in args)), 'Expected non-empty sets'
    original_set = set.union(*args)
    return original_set