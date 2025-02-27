def sum_ints_div_by_either_nums(int_list):
    sum_44_to_59 = sum((x for i, x in enumerate(int_list[44:60]) if x % 39 == 0 or x % 15 == 0))
    return sum_44_to_59