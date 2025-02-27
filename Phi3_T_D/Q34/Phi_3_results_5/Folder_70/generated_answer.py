def find_original_set(*args):
    original = set().union(*args)
    return original if len(args) == 312 else 'Incorrect number of sets'