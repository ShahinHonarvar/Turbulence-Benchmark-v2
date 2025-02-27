def find_original_set(*args):
    assert len(args) == 15, 'Invalid number of arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Arguments should be sets'
    assert all((len(arg) > 0 for arg in args)), 'Arguments should not be empty sets'
    assert all((all((isinstance(item, int) for item in arg)) for arg in args)), 'Arguments should contain only integers'
    assert len(set((arg for arg in args))) == len(args), 'Arguments should be distinct'
    original_set = set.union(*args)
    return original_set