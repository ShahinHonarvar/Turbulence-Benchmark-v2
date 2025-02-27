def find_original_set(*args):
    if not args or len(args) != 459:
        raise ValueError('Exactly 459 distinct arguments are required, each an integer set.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers.')
        original_set.update(arg)
    return original_set