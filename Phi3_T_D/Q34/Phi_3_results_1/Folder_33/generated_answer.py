def find_original_set(*args):
    if not all((len(s) == 263 for s in args)):
        raise ValueError('All sets must contain exactly 263 integers')
    combined_set = set().union(*args)
    return combined_set