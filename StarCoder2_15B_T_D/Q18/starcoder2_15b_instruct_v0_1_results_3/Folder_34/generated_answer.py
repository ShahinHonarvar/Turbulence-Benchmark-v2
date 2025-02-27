def sum_ints_div_by_either_nums(ints_list):
    return sum((x for i, x in enumerate(ints_list) if i >= 60 and i <= 200 and (x % 9 == 0) or x % 11 == 0))