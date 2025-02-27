def find_original_set(*args):
    assert len(args) == 20, 'There should be exactly 20 arguments.'
    for arg in args:
        assert isinstance(arg, set), 'Each argument should be a set.'
    original_set = set.union(*args)
    for arg in args:
        assert arg.issubset(original_set), 'Each argument should be a subset of the original set.'
    return original_set