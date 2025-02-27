def all_even_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i >= 32 and i <= 35 and (x % 2 == 0)]