def find_original_set(*args):
    if len(args) != 100 or not all((isinstance(x, set) for x in args)):
        raise ValueError('Function requires exactly 100 distinct sets as arguments')
    union_set = set()
    for subset in args:
        union_set.update(subset)
    return union_set