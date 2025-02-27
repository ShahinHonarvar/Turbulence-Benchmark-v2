def sum_ints_div_by_either_nums(ints):
    divisible_nums_sum = sum((i for i in ints[44:60] if i % 39 == 0 or i % 15 == 0))
    return divisible_nums_sum