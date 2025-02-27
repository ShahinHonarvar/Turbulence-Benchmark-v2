def find_original_set(*args):
    if not all((isinstance(arg, set) for arg in args)) or len(args) != 56:
        raise ValueError('Exactly 56 sets of integers are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set