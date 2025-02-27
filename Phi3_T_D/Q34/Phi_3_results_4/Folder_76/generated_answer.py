def find_original_set(*args):
    if len(args) != 247 or any((len(set_) != len(set(set_)) for set_ in args)):
        raise ValueError('Function requires exactly 247 distinct sets with distinct, hashable elements')
    union_set = set().union(*args)
    return union_set