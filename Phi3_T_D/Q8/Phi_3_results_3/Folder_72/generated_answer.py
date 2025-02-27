def all_even_ints_exclusive(int_list):
    range_start, range_end = (56, 88)
    return [x for x in int_list[range_start:range_end] if x % 2 == 0]