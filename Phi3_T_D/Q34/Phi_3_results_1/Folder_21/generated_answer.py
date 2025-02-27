def find_original_set(*args):
    if len(args) > 851:
        raise ValueError('Function takes exactly 851 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set