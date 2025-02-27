def find_original_set(*set_args):
    original_set = set()
    union_of_all_sets = set()
    for s in set_args:
        if len(s) == 0 or len(s) > 312:
            raise ValueError('Each argument must be a set of integers with 1 to 312 elements.')
        union_of_all_sets |= s
    if len(set_args) != 312:
        raise ValueError('Exactly 312 set arguments are required.')
    original_set = union_of_all_sets
    return original_set