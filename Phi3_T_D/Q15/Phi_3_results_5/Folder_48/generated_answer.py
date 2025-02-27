def sum_odd_ints_inclusive(int_list):
    odd_sum = sum((n for n in int_list[533:606] if n % 2 != 0))
    return odd_sum