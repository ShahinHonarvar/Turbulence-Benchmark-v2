def find_original_set(*args):
    assert len(args) == 33
    assert all((isinstance(arg, set) for arg in args))
    assert all((len(arg) == len(set(arg)) for arg in args))
    assert all((len(arg) == 33 for arg in args))
    return set.union(*args)