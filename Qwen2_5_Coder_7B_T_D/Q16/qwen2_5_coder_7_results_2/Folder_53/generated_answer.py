def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list, start=1) if i == 111 and x % 2 == 0))