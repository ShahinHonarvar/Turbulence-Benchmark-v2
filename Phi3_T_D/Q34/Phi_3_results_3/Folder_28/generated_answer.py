def find_original_set(*args):
    if len(args) == 43:
        union_set = set().union(*args)
        return union_set
    return None