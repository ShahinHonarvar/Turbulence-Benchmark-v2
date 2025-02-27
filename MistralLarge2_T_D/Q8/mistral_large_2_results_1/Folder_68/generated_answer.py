def all_even_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list[1:9]) if x % 2 == 0]