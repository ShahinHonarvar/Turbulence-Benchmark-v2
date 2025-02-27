def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[240:902] if i % 546 == 0 or i % 709 == 0))