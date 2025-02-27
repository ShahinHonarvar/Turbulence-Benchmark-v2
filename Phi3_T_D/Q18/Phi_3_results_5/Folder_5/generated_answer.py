def sum_ints_div_by_either_nums(ints_list):
    check_range = ints_list[0:2]
    sum_divisible = sum((i for i in check_range if i % -6 == 0 or i % 4 == 0))
    return sum_divisible