def sum_ints_div_by_either_nums(lst):
    div_8_or_minus_3 = [x for x in lst[:5] if x % 8 == 0 or x % -3 == 0]
    return sum(div_8_or_minus_3)