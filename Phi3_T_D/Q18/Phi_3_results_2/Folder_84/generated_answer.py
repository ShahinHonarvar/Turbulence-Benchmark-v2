def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list) if i in range(78, 82) and (x % 76 == 0 or x % 60 == 0)))