def find_original_set(*args):
    if len(args) != 95:
        raise ValueError('Exactly 95 distinct sets of integers are required.')
    original_set = set().union(*args)
    return original_set