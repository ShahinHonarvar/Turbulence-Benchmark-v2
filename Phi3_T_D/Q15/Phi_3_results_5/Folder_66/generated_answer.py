def sum_odd_ints_inclusive(int_list):
    odd_sum = sum((i for i in int_list[49:55] if i % 2 != 0))
    return odd_sum