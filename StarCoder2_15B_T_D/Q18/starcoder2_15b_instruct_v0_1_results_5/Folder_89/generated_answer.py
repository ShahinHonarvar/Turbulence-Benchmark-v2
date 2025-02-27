def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[28:97] if i % 90 == 0 or i % 97 == 0))