def find_original_set(*args):
    assert len(args) == 90, 'Expected 90 arguments, got {}'.format(len(args))
    original_set = set.union(*args)
    for arg in args:
        assert arg.issubset(original_set), 'Argument {} is not a subset of the original set'.format(arg)
    return original_set