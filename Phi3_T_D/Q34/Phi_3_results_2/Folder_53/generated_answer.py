def find_original_set(*args):
    if len(args) == 84:
        union_set = set()
        for arg in args:
            union_set |= arg
        return union_set
    else:
        raise ValueError('Exactly 84 arguments are required.')