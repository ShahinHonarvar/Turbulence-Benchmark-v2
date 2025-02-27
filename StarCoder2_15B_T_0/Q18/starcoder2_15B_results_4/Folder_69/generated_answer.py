def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[61:89] if i % 31 == 0 or i % 11 == 0))