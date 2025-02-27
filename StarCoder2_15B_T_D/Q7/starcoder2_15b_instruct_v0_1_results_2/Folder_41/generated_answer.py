def all_even_ints_inclusive(ints_list):
    return [x for x in ints_list if x % 2 == 0 and 6 <= ints_list.index(x) <= 6]