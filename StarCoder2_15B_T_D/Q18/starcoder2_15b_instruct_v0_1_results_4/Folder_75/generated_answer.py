def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[20:94] if i % -92 == 0 or i % -50 == 0))