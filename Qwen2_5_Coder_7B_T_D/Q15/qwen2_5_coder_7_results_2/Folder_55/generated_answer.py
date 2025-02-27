def sum_odd_ints_inclusive(num_list):
    return sum((x for i, x in enumerate(num_list[:11]) if i <= 10 and x % 2 != 0))