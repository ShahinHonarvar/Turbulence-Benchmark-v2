def all_even_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i in range(2, 6) and x % 2 == 0]