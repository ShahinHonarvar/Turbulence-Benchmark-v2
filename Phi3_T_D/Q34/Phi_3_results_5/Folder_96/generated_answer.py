def find_original_set(*args):
    return set.union(*args) if all((isinstance(arg, set) for arg in args)) and len(set(map(len, args))) == 1 else None