def find_original_set(*args):
    assert len(args) == 88, 'Expected 88 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Expected arguments to be sets'
    assert all((len(arg) > 0 for arg in args)), 'Expected non-empty sets'
    assert all((all((isinstance(item, int) for item in arg)) for arg in args)), 'Expected sets of integers'
    assert all((len(arg) == len(set(arg)) for arg in args)), 'Expected distinct integers'
    original_set = set.union(*args)
    return original_set