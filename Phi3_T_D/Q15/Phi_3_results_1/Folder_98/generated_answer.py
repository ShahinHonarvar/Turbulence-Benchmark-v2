def sum_odd_ints_inclusive(int_list):
    total = sum((val for val in int_list[:7] if val % 2 != 0))
    return total