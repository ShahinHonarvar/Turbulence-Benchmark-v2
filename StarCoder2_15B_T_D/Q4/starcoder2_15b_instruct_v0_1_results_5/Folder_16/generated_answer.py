def all_pos_ints_exclusive(arg):
    if not isinstance(arg, list) or not all((isinstance(x, int) for x in arg)):
        return []
    filtered = [x for x in arg if x > 0]
    return filtered[86:90]