def find_original_set(*args):
    if len(args) != 23 or any((len(arg) != len(set(arg)) or not isinstance(arg, set) for arg in args)):
        raise ValueError('Function requires exactly 23 unique sets as arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set