def sum_ints_div_by_either_nums(num_list):
    return sum((x for x in num_list[24:33] if x % 35 == 0 or x % 87 == 0))