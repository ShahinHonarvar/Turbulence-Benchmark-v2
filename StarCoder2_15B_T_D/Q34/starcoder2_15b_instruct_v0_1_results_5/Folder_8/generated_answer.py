def find_original_set(*args):
    assert len(args) == 45
    assert all((isinstance(arg, set) for arg in args))
    original_set = set.union(*args)
    return original_set