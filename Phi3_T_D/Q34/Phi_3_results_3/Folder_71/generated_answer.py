def find_original_set(*args):
    if len(args) != 16:
        return 'Exactly 16 distinct sets are required'
    union_set = set().union(*args)
    return union_set