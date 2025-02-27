def sum_odd_ints_inclusive(int_list):
    odd_sum = sum((x for x in int_list[6:9] if x % 2 != 0))
    return odd_sum