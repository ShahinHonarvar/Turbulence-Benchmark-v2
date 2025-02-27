def sum_ints_div_by_either_nums(input_list):
    return sum((x for i, x in enumerate(input_list) if i >= 68 and i <= 99 and (x % -37 == 0) or x % -26 == 0))