def sum_ints_div_by_either_nums(integers):
    subset = integers[57:85]
    divisible_sum = sum((i for i in subset if i % -30 == 0 or i % -88 == 0))
    return divisible_sum