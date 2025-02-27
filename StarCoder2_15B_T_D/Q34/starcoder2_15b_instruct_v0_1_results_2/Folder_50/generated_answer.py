def find_original_set(*args):
    assert len(args) == 99
    assert all((isinstance(arg, set) for arg in args))
    assert all((len(arg) > 0 for arg in args))
    assert all((isinstance(x, int) for arg in args for x in arg))
    assert all((x == y for arg in args for x, y in zip(sorted(arg), sorted(arg))))
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Each argument must be a subset of the original set.')
    return original_set