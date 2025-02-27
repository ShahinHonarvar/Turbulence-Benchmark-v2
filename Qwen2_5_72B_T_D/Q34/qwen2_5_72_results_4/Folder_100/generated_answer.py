def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('The function requires exactly 91 distinct sets as arguments.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set