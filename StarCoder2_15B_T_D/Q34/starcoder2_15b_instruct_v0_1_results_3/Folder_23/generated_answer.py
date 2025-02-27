def find_original_set(*args):
    assert len(args) == 41
    assert all((isinstance(arg, set) for arg in args))
    assert all((len(arg) == len(args[0]) for arg in args))
    return set.union(*args)