def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Please provide exactly 45 sets')
    original_set = set().union(*args)
    return original_set