def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 sets are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be of type set.')
        original_set.update(arg)
    return original_set