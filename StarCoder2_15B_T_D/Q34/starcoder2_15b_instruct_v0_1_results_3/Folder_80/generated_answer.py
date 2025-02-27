def find_original_set(*args):
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets'
    assert len(args) == 453, 'There must be exactly 453 arguments'
    original_set = set.union(*args)
    return original_set