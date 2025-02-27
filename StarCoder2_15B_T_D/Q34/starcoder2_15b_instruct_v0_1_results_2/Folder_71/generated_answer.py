def find_original_set(*args):
    assert len(args) == 16, 'Expected exactly 16 arguments'
    assert all((isinstance(arg, set) for arg in args)), 'Expected each argument to be a set'
    assert all((len(arg) == len(args[0]) for arg in args)), 'Expected all arguments to have the same length'
    assert all((isinstance(elem, int) for arg in args for elem in arg)), 'Expected each element to be an integer'
    assert len(set((elem for arg in args for elem in arg))) == len(args[0]), 'Expected all elements to be distinct'
    original_set = set.union(*args)
    return original_set