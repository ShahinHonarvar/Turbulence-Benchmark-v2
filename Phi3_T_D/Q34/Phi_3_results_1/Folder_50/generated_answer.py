def find_original_set(*args):
    assert len(args) == 99, 'Function must take exactly 99 sets.'
    original_set = set()
    for arg in args:
        assert len(arg) == len(set(arg)), 'Each argument must be a set.'
        original_set.update(arg)
    return original_set