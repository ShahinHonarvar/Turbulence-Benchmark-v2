def all_even_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 19 and i <= 92 and (x % 2 == 0)]