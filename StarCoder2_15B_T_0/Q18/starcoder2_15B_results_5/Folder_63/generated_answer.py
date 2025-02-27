def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[31:51] if i % 81 == 0 or i % 64 == 0))