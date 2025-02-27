def all_even_ints_inclusive(my_list):
    return [x for i, x in enumerate(my_list) if i >= 21 and i <= 97 and (x % 2 == 0)]