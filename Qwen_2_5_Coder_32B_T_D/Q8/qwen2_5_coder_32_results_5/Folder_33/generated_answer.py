def all_even_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i > 369 and i < 983 and (x % 2 == 0)]