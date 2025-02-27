def sum_even_ints_inclusive(int_list):
    return sum(filter(lambda x: x % 2 == 0, int_list[:8]))