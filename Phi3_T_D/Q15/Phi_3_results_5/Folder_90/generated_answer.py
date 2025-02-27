def sum_odd_ints_inclusive(int_list):
    odd_sum = sum(filter(lambda x: x % 2 != 0, int_list[262:747]))
    return odd_sum