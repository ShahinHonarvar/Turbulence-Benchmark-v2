def all_even_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if i % 2 == 0 and 19 <= i <= 92]