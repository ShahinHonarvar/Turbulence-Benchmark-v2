def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 sets are required as arguments.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(item, int) for item in arg)):
            raise ValueError('All arguments must be sets of integers.')
        result_set.update(arg)
    return result_set