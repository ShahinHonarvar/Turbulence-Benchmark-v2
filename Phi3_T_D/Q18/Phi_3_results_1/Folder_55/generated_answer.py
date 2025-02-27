def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[:10] if i % 10 == 0 or i % 100 == 0))