def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[54:80] if i % 54 == 0 or i % 28 == 0))