def all_even_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 13 <= i < 66 and x % 2 == 0]