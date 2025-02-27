def find_original_set(*args):
    if len(args) != 16:
        return 'Input must be exactly 16 sets.'
    original_set = set().union(*args)
    return original_set