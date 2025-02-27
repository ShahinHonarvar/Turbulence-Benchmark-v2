def sum_even_ints_inclusive(int_list):
    return sum((val for idx, val in enumerate(int_list[37:52]) if val % 2 == 0))