def all_even_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 20 < i < 51 and x % 2 == 0]