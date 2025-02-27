def find_original_set(*args):
    if len(args) != 702:
        raise ValueError('Exactly 702 sets are required.')
    original_set = set()
    for arg in args:
        if not all((isinstance(item, int) for item in arg)):
            raise ValueError('All elements in the sets must be integers.')
        original_set.update(arg)
    return original_set