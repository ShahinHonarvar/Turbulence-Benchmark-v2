def sum_odd_ints_inclusive(int_list):
    return sum(filter(lambda x: x % 2 == 1, int_list[22:64]))