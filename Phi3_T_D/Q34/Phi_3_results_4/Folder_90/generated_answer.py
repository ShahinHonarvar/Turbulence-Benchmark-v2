def find_original_set(*args):
    if len(args) != 985:
        raise ValueError('Exactly 985 distinct arguments are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set