def all_even_ints_inclusive(my_list):
    return [x for i, x in enumerate(my_list) if i >= 37 and i <= 76 and (x % 2 == 0)]