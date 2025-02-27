def find_original_set(*args):
    assert len(args) == 132, 'Invalid number of arguments'
    assert all((isinstance(arg, set) for arg in args)), 'All arguments must be sets'
    assert all((len(arg) > 0 for arg in args)), 'All sets must contain at least one element'
    original_set = set.union(*args)
    return original_set