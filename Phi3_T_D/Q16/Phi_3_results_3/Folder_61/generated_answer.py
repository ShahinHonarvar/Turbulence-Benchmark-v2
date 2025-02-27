def sum_even_ints_inclusive(int_list):
    return sum((i for i in int_list[:8])) if any((i % 2 == 0 for i in int_list[:8])) else 0