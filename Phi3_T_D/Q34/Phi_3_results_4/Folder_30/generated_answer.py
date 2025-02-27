def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError("All arguments must be of type 'set'")
        if not all((isinstance(e, int) for e in arg)):
            raise ValueError('All sets must contain only integers')
        original_set.update(arg)
    return original_set