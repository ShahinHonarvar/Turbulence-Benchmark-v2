def sum_ints_div_by_either_nums(ints):
    return sum(filter(lambda x: x % 82 == 0 or x % 90 == 0, ints[41:57]))