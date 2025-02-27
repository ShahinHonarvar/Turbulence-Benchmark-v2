def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 set arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError(f'Argument {arg} is not a set')
        original_set.update(arg)
    return original_set