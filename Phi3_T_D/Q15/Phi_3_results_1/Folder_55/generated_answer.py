def sum_odd_ints_inclusive(int_list):
    total = sum((n for n in int_list[:11] if n % 2 != 0))
    return total