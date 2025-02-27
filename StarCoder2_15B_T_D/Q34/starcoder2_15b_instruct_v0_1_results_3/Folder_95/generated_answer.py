def find_original_set(*args):
    assert len(args) == 88
    assert all((isinstance(arg, set) for arg in args))
    assert all((len(arg) > 0 for arg in args))
    assert all((isinstance(x, int) for arg in args for x in arg))
    assert all((len(arg) == len(set(arg)) for arg in args))
    smallest_set = set.union(*args)
    return smallest_set