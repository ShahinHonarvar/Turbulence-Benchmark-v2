def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 sets are required.')
    original_set = args[0]
    for arg in args[1:]:
        original_set.update(arg)
    return original_set